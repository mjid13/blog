from django.shortcuts import render

# Create your views here.
from .models import IndexPage


# from .forms import BannerForm


def index(request):
    banner_text = IndexPage.objects.first()  # Assuming there's only one banner text
    print(banner_text)
    # form = BannerForm(instance=banner_text)
    # if request.method == 'POST':
    #     form = BannerForm(request.POST, instance=banner_text)
    #     if form.is_valid():
    #         form.save()

    return render(request=request,
                  template_name='index.html',
                  context={'banner_text': banner_text})
