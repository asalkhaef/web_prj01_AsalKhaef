from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Banner
from django.contrib.sessions.models import Session


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['headBanner'] = Banner.objects.get(banner_type='head_banner')
        context['adBanner'] = Banner.objects.get(banner_type='ad_banner')
        context['signup_form'] = CustomUserCreationForm()
        context['login_form'] = AuthenticationForm()
        return context

    def post(self, request, *args, **kwargs):
        print(request.POST)
        type1 = request.POST.get('type')
        if type1 == 'signup':
            if request == request.POST:
                print("signup")
                signup_form = CustomUserCreationForm(request.POST)
                if signup_form.is_valid():
                    print("valid")
                    signup = signup_form
                    signup_form.save()
                    # print(signup_form)
                    # After successful signup, redirect to success URL
                    return render(request, self.template_name, {
                        'signup_form': signup,
                        'headBanner': Banner.objects.get(banner_type='head_banner'),
                        'adBanner': Banner.objects.get(banner_type='ad_banner')
                    })
                else:
                    # If form is not valid, re-render the template with the form errors
                    return render(request, self.template_name, {
                        'signup_form': signup_form,
                        'login_form': AuthenticationForm(),
                        'headBanner': Banner.objects.get(banner_type='head_banner'),
                        'adBanner': Banner.objects.get(banner_type='ad_banner')
                    })
        elif type1 == 'login':
            login_form = AuthenticationForm(data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                # After successful login, redirect to success URL
                return render(request, self.template_name, {
                    'headBanner': Banner.objects.get(banner_type='head_banner'),
                    'adBanner': Banner.objects.get(banner_type='ad_banner')
                })
            else:
                # If login form is not valid, re-render the template with the form errors
                return render(request, self.template_name, {
                    'login_form': AuthenticationForm(),
                    'headBanner': Banner.objects.get(banner_type='head_banner'),
                    'adBanner': Banner.objects.get(banner_type='ad_banner')
                })

        # Ensure a default response is returned if neither 'signup' nor 'login' is in request.POST
        # In this case, redirect to the success URL or render the template with initial context

    def get_success_url(self):
        return reverse('home')


class ProductPageView(TemplateView):
    template_name = 'product.html'

# def login_view(request):
#     login_form = AuthenticationForm(data=request.POST)
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         print(user)
#         if user[username] != "":
#             print("ada")
#             login(request, user)
#             request.session['username'] = username
#             request.session.save()
#             return render(request, 'home-page.htm')
