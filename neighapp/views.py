from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your account has been created successfully')
            return redirect('home_view')
        else:
            form = UserCreationForm()
    context = {
        'form':form,
    }
    return render(request,context)
