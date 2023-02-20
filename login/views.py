from django.shortcuts import render
from django.http import HttpResponse

# from django.contrib.auth.views import LoginView

# Create your views here.

def home(request):
    return render(request,'home.html')


# class ManagementLoginView(LoginView):
#     template_name = 'app_name/management_login.html'

#     def form_valid(self, form):
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password')
#         management_code = form.cleaned_data.get('management_code')
#         user = authenticate(self.request, username=username, password=password)
#         if user and user.is_staff and management_code == 'your_management_code_here':
#             login(self.request, user)
#             return redirect('dashboard')
#         else:
#             return self.form_invalid(form, error_message='Invalid login credentials')
