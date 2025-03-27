from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def blog_list(request):
    return render(request, 'core/blog_list.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

def faqs(request):
    return render(request, 'core/faqs.html')