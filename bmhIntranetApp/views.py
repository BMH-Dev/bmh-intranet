from django.shortcuts import render

# Create your views here.
def demo(request):
    data = range(1, 10)
    return render(request, 'dashboard.html', {'numg': data})
