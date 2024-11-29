from django.forms import BaseModelForm
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from CarBlog.models import Car, Comment
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from CarBlogFrontend.forms import CarForm, CommentForm
from django.shortcuts import render, redirect


class CarListView(ListView):
    """
    Контролер для отображения всех авто через интерфейс.
    """
    model = Car
    template_name = 'CarBlog/CarBlog.html'


class CarCreateView(LoginRequiredMixin, CreateView):
    """
    Контролер для создания авто через интерфейс.
    """
    model = Car
    form_class = CarForm
    success_url = reverse_lazy('carblog:main')
    template_name = 'CarBlog/car_form.html'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        car = form.save()
        car.owner = self.request.user
        car.save()
        return super().form_valid(form)


class CarUpdateView(LoginRequiredMixin, UpdateView):
    """
    Контролер для изменения авто через интерфейс.
    """
    model = Car
    form_class = CarForm
    success_url = reverse_lazy('carblog:main')
    login_url = reverse_lazy('user:login')
    template_name = 'CarBlog/car_form.html'
    

class CarDeleteView(LoginRequiredMixin, DeleteView):
    """
    Контролер для удаления авто через интерфейс.
    """
    success_url = reverse_lazy('carblog:main')
    login_url = reverse_lazy('user:login')
    redirect_field_name = 'redirect_to'
    model = Car
    template_name='CarBlog/car_delete_confirm.html'


class CarTemplateView(LoginRequiredMixin, TemplateView):
    """
    Контролер для отображения одного авто и дабавления комментарий к нему через интерфейс.
    """
    model = Comment
    login_url = reverse_lazy('user:login')
    redirect_field_name = 'redirect_to'
    template_name = 'CarBlog/car.html'

    def get(self, request, pk):
        car_item = Car.objects.get(pk=pk)
        context = {'object': car_item, 'comments': Comment.objects.filter(car=car_item), 'comment_form':CommentForm()}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        car_item = Car.objects.get(pk=self.kwargs['pk'])
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = self.request.user
            comment.car = car_item
            comment.save()
            return redirect('carblog:car', pk=car_item.pk)
        return self.get(request, car_item.pk)
        