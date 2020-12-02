from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your account has been created successfully')
            return redirect('home_view')
        else:
            form = RegistrationForm()
    context = {
        'form':form,
    }
    return render(request,context)
