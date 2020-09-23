from django.shortcuts import render, HttpResponse
from .models import Work

from django.core.paginator import Paginator


# Create your views here.
def index(request):
    work_list = Work.objects.all()
    paginator = Paginator(work_list, 1)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'page_obj': page_obj})


def work_detail(request, pk):
    work = Work.objects.get(pk=pk)
    content = {
        'work': work
    }
    return render(request, 'details.html', content)


def about(request):
    with open('ReadMe.md', 'r') as file:
        return HttpResponse(file.readlines())


def rules(request):
    return HttpResponse("1. don't have ruele")
