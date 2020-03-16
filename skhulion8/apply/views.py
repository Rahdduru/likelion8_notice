from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'apply/home.html')

def guide(request):
    return render(request, 'apply/guide.html')

def faq(request):
    return render(request, 'apply/faq.html')