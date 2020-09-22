from django.shortcuts import render
from .models import Work

from django.core.paginator import Paginator


# Create your views here.
def index(request):
    works = Work.objects.all()
    content = {
        'works': works
    }
    return render(request, 'index.html', content)


def listing(request):
    work_list = Work.objects.all()
    paginator = Paginator(work_list, 1)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'work_list.html', {'page_obj': page_obj})


def work_detail(request, pk):
    work = Work.objects.get(pk=pk)
    content = {
        'work': work
    }
    return render(request, 'work_detail.html', content)
