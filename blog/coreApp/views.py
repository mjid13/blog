from django.shortcuts import render

# Create your views here.
from .models import *


# from .forms import BannerForm


def index(request):
    index_text = IndexPage.objects.first()  # Assuming there's only one banner text
    # form = BannerForm(instance=banner_text)
    # if request.method == 'POST':
    #     form = BannerForm(request.POST, instance=banner_text)
    #     if form.is_valid():
    #         form.save()
    print(index_text.logo)
    return render(request=request,
                  template_name='index.html',
                  context={'index_text': index_text})

def about(request):
    about_text = aboutPage.objects.first()
    print(about_text.photo1)
    return render(request=request,
                  template_name='about.html',
                  context={'about_text':about_text})

def contact(request):

    return render(request=request,
                  template_name='contact.html',
                  context={})