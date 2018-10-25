#aws ses
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template

from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.views.generic import View, FormView, CreateView, DetailView

from newsletter.forms import JoinForm
from .models import Page

from .forms import ContactForm, LoginForm, RegisterForm

# class HomeView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, "pages/home.html", {})



class HomeView(SuccessMessageMixin, CreateView):
    template_name = 'pages/home.html'
    form_class  = JoinForm
    success_url = '/'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        # context['object'] = Page.objects.order_by("?").first()
        context['object'] = Page.objects.filter(featured=True).first() # with featured activated in the model
        return context

    def get_success_message(self, cleaned_data):
        # print(cleaned_data)
        return "Thank you for joining!"

    # def form_valid(self, form):
    #     email = form.cleaned_data.get("email")
    #     # other things with email
    #     return super(HomeView, self).form_valid(form)



class PageDetailView(DetailView):
    queryset = Page.objects.filter(active=True)
    model = Page
    template_name = 'pages/home.html'


def contact_page(request):
    form = ContactForm(request.POST or None)
    template = "contact/view.html"

    if form.is_valid():
        username = form.cleaned_data.get("fullname")
        email = form.cleaned_data.get("email")
        content = form.cleaned_data.get("content")
        print(username)
        print(email)
        print(content)


        send_mail(
            'Contact Us',
            content,
            email,
            ['caesar.orz@gmail.com'],
            fail_silently=False,
        )

    context = {
        "form": form
    }
    return render(request, template, context)
