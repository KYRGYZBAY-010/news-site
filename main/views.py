from django.shortcuts import render, redirect
from pkg_resources import working_set
from main.models import HomeNews, About
from django.views.generic import DetailView, UpdateView
from .forms import HomeNewsForm


def index(request):
    homenews = HomeNews.objects.order_by('-date')
    return render(request, 'main/index.html', {'homenews': homenews})


def about(request):
    abouts = About.objects.all()
    return render(request, 'main/about.html', {'abouts': abouts})


class HomeDetail(DetailView):
    model = HomeNews
    template_name = 'main/details_main.html'
    context_object_name = 'home'



class HomeUpdate(UpdateView):
    model = HomeNews
    template_name = 'main/update.html'

    fields = ['img','title','description','date']
    success_url ="/"


def creates(request):

    error = ''
    if request.method == 'POST':
        print('enter')
        form = HomeNewsForm(request.POST, request.FILES)
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