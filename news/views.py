from django.shortcuts import render


def home(request):
    return render(request,'news/pages/home.html', context={
        'name': 'teste',
    })
