from django.shortcuts import render, redirect

# Create your views here.
from .models import ShortURL


def home(request):
    # context = {'name': 'Anant'}
    if request.method == "POST":
        print(request.POST.get('url'))
        url = request.POST.get('url')
        key_word = request.POST.get('surl')
        short_url = f"https://shortlinkproject.herokuapp.com/{key_word}"
        ShortURL(main_url=url, short_url=short_url).save()
        context = {
            'url': short_url,
            'surl': key_word
        }
        return render(request, 'url_shortener/url.html',context)
    else:
        return render(request, 'url_shortener/q.html')


def shorturl(request, surl):
    print(surl)
    surl1 = f"https://shortlinkproject.herokuapp.com/{surl}"
    print(surl1)
    q = ShortURL.objects.get(short_url=surl1)
    return redirect(q.main_url)
