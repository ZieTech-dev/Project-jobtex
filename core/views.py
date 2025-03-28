from django.shortcuts import render

def home(request):
    context = {
        'page_home':'active'
    }
    return render(request, 'core/home.html',context)

def blog_list(request):
    context = {
        'page_blog':'active'
    }
    return render(request, 'core/blog_list.html',context)

def about(request):
    context = {
        'page_about':'active'
    }
    return render(request, 'core/about.html',context)

def contact(request):
    context = {
        'page_contact':'active'
    }
    return render(request, 'core/contact.html',context)

def faqs(request):
    context = {
        'page_faqs':'active'
    }
    return render(request, 'core/faqs.html',context)