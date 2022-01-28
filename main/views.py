from django.shortcuts import render, HttpResponseRedirect
from .models import Post, Contact
from .forms import ContactForm
from datetime import datetime


def home(request):
    obj = Post.objects.all().order_by('-id')
    data = {
        'p1': obj[0],
        'p2': obj[1],
        'p3': obj[2],
    }
    return render(request, 'home.html', data)

def post(request, name):
    ls = Post.objects.get(link_title=name)
    data = {
        'title': ls.title,
        'data': ls.data,
        'topics': ls.topic,
        'date': ls.date,
    }
    return render(request, 'post.html', data)

def blog(request, topic=None):
    obj = Post.objects.all().order_by('-id')
    if topic:
        ls = []
        for i in obj:
            if topic.upper() in i.topic.upper():
              ls.append(i)
        d = {"item": ls}
    else:
        d = {"item": obj}
    return render(request, "blog.html", d)

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            content = form.cleaned_data['content']
            date = datetime.today().strftime('%B %d, %Y %H:%M')

            d = Contact(name=name, email=email, subject=subject, content=content, date=date)
            d.save()

            return HttpResponseRedirect('/contact/thank-you/')
    else:
        form = ContactForm()
        return render(request, 'contact.html', {"form": form})

def thank_you(request):
    return render(request, 'thank-you.html')

def about_me(request):
    return render(request, 'base.html')
