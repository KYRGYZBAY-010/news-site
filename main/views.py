from django.shortcuts import render, redirect
from pkg_resources import working_set
from main.models import HomeNews, About
from django.views.generic import DetailView 
from .forms import HomeNewsForm


def index(request):
    homenews = HomeNews.objects.order_by('-date')
    print(homenews)
    return render(request, 'main/index.html', {'homenews': homenews})


def about(request):
    abouts = About.objects.all()
    return render(request, 'main/about.html', {'abouts': abouts})


def creates(request):

    error = ''
    if request.method == 'POST':
        form = HomeNewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = HomeNewsForm()
    data = {
        'forms': form,
        'error': error
    }
    return render(request, 'main/creates.html', data)

def community(request):
    return render(request, 'main/community.html')



class HomeDetail(DetailView):
    model = HomeNews
    template_name = 'main/details_main.html'
    context_object_name = 'home'