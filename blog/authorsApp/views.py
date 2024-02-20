from django.shortcuts import render
from .models import Profile
from .forms import RegistrationForm
# Create your views here.


# views.py
from django.shortcuts import render, redirect
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to the homepage after successful registration
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
