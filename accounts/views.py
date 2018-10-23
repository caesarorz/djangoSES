from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url
from django.views.generic import View, FormView, CreateView, DetailView
from .forms import LoginForm, RegisterForm
from django.http import HttpResponse


# Create your views here.


class LoginView(FormView):
    form_class = LoginForm
    template_name = "auth/login.html"
    success_url = "/"

    def form_valid(self, form):
        request = self.request
        next_ = request.GET.get('next')
        next_post = request.POST.get('next')
        redirect_path = next_ or next_post or None

        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect("/")
        return super(LoginView, self).form_invalid(form)
#
# def login_page(request):
#     form = LoginForm(request.POST or None)
#     template = "auth/login.html"
#     context = {'form': form}
#
#     print(request.user.is_authenticated)
#
#     next_ = request.GET.get('next')
#     next_post = request.POST.get('next')
#     redirect_path = next_ or next_post or None
#
#     if form.is_valid():
#         print(request.user.is_authenticated)
#         print(form.cleaned_data)
#         username = form.cleaned_data.get("username")
#         password = form.cleaned_data.get("password")
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             print(request.user.is_authenticated)
#             login(request, user)
#             context['form'] = LoginForm()
#             if is_safe_url(redirect_path, request.get_host()):
#                 return redirect(redirect_path)
#             else:
#                 return redirect("/")
#         else:
#             print("Error")
#     return render(request, template, context)


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "auth/register.html"
    success_url = "/login"

# User = get_user_model()
# def register_page(request):
#     form = RegisterForm(request.POST or None)
#     template = "auth/register.html"
#     context = {'form': form}
#
#     print(request.user.is_authenticated)
#     if form.is_valid():
#         print(form.cleaned_data)
#         username = form.cleaned_data.get("username")
#         email = form.cleaned_data.get("email")
#         password = form.cleaned_data.get("password")
#         # new_user = User.objects.create_user(username, email, password)
#         form.save()
#         # print(new_user)
#     return render(request, template, context)
