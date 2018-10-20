from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .models import *

def index(request):
    context = {'courses': Course.objects.all()}
    return render(request, 'courses/index.html', context)

def add(request):
    name = request.POST['name']
    desc = request.POST['description']

    errors = Course.objects.validate_form(request.POST)

    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error)
        return redirect('/')
    else: 
        description = Description.objects.create(description=desc)
        Course.objects.create(name=name, description=description)

    return redirect('/')

def show(request, id):
    try: 
        c = Comment.objects.filter(course=id)
    except ObjectDoesNotExist:
        c = None

    context = {
        'course': Course.objects.get(id=id),
        'comments': c
    }

    return render(request, 'courses/show.html', context)

def add_comment(request, id):
    name = request.POST['name']
    comment = request.POST['comment']

    errors = Comment.objects.validate_comment_form(request.POST)

    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error)
        return redirect('/courses/'+str(id))
    else:
        Comment.objects.create(name=name, comment=comment, course=Course.objects.get(id=id))
        return redirect('/courses/'+str(id))

def confirm_delete(request, id):
    context = {'course': Course.objects.get(id=id)}
    return render(request, 'courses/confirm_delete.html', context)

def destroy(request, id):
    Course.objects.get(id=id).delete()
    return redirect('/')