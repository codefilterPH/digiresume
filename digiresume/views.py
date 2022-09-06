from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.
def home(request):
    me = Me.objects.get(id=1)
    skills = CodingSkill.objects.all()
    frameworks = Frameworks.objects.all()
    rate = CodingSkill.objects.filter(percentage__gt=90)
    portfolio = Portfolio.objects.all()
    cert = Certificates.objects.all()
    testimony = Testimonials.objects.all()
    leastToGreatest = Portfolio.objects.all().order_by('date_created')
    context = {
        'me':me, 'skills':skills, 'frameworks':frameworks,'rate':rate,
        'portfolio':portfolio, 'certificates':cert, 'testimonials':testimony,
        'recent':leastToGreatest
    }
    return render(request, 'main/index.html', context)
def blog(request):
    links = Blogs_Links.objects.all()
    context = {'links':links}
    return render(request, 'main/blog.html', context)
def blog_detail(request):
    return render(request, 'main/blog-detail.html')
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/digiresume/message/')
    else:
        form = ContactForm()
    return render(request, 'main/contact.html',{'form': form})

def portfolio(request):
    portfolio = Portfolio.objects.all()
    context = {'portfolio':portfolio}
    return render(request, 'main/portfolio.html', context)

def portfolio_detail(request):
    return render(request, 'main/portfolio-detail.html')

def save_clients(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            p = Clients(name=name, email=email, message=message)
            p.save()
            return HttpResponseRedirect('/digiresume/')
    return render(request, 'main/index.html')
