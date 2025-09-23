from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/index.html')


def handler404(request, exception):
    return render(request, 'home/404.html', status=404)
