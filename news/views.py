from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView


def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news_home.html', {'news': news})


class NewsDetalView(DetailView):
    model = Articles
    template_name = 'details_view.html'
    context_object_name = 'article'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма была неверной'

    form = ArticlesForm()
    date = {
        'form': form,
        'error': error
    }
    return render(request, 'create.html', date)