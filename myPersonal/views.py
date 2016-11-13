from django.shortcuts import render

def index(request):
    return render(request, 'myPersonal/home.html')


def contact(request):
    return render(request, 'myPersonal/basic.html', {'content':["If you'd like to contact me", "yanirash@yahoo.fr"]})