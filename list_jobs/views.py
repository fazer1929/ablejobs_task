from list_jobs.models import Job
from django.contrib.auth import authenticate,login
from django.views import generic,View
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import LoginForm, RegisterForm,JobForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.contrib import messages

class LoginView(View):
    form_class = LoginForm
    template_name='list_jobs/login.html'
    def get(self,request):
        form = self.form_class()
        return render(request,'list_jobs/login.html', {'form': form})
    def post(self,request):
        form = self.form_class(request.POST)
        print("\n\n\n")
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                if(user.is_staff):
                    return redirect('joblist')
                else:
                    return redirect('home')

            return render(request,self.template_name)
            
        messages.error(request, 'Please check your username or email')
        return render(request, self.template_name, {'form': form})



class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'list_jobs/register.html'
    success_url = reverse_lazy('login')



class HomeView(LoginRequiredMixin ,View):
    login_url='/login'
    form_class = JobForm
    template_name='list_jobs/home.html'
    def get(self,request):
        form = self.form_class()
        return render(request,'list_jobs/home.html', {'form': form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.owner = request.user
            job.save()
            messages.success(request, 'Form submission successful')
            return HttpResponseRedirect('/')
        
        messages.error(request, 'Errors in forms')
        return render(request, self.template_name, {'form': form})


class JobListView(LoginRequiredMixin ,View):
    login_url='/login'
    template_name='list_jobs/job_list.html'

    def get(self,request):
        if(request.user.is_staff):
            jobList = Job.objects.all()
            return render(request,self.template_name,{"jobList":jobList})

        else:
            return HttpResponseRedirect('/')
        
def logoutView(request):
    if(request.user != None):
        logout(request)
    
    return redirect('login')