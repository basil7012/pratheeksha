from django.shortcuts import render, get_object_or_404
from  .models import *
from datetime import date
from django.core.paginator import Paginator,EmptyPage,InvalidPage

# Create your views here.
def home(request):
    catog=category.objects.all()
    return render(request,'index.html',{'cat':catog})

def details(request,category_id):
    ct=category.objects.get(id=category_id)


    prod=number.objects.filter(categorys=category_id).order_by('-date')
    paginator = Paginator(prod, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        pro = paginator.page(page)
    except(EmptyPage, InvalidPage):
        pro = paginator.page(paginator.num_pages)
    return render(request,'lottery_details.html',{'pro':prod,'pg':pro,'ct':ct})


def add_details(request,category_id):
    prod = category.objects.get(id=category_id)
    if request.method == 'POST':
        if request.POST.get('date') :
            post = number()

            post.date = request.POST.get('date')
            post.number1 = request.POST.get('number1')
            post.number2 = request.POST.get('number2')
            post.number3 = request.POST.get('number3')
            post.categorys=prod
            post.save()
    return render(request,'add_details.html',{'pr':prod})

def searching(request):
    prod=None
    query=None


    if 'q' in request.GET:
        query=request.GET.get('q')


        prod=number.objects.filter(date__contains=query)





    return render(request,'search.html',{'qr':query,'prod':prod})
