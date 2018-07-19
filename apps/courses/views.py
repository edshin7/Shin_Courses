from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Course, Description

# Create your views here.
def index(request):
    return render(request, "index.html", { "courses": Course.objects.all().values() })

def add(request):
    errors = Course.objects.validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)

            return redirect("/courses")

    newCourse = Course.objects.create(name=request.POST["name"], description=request.POST["content"])
    return redirect("/courses")

def toDestroy(request, id):
    return redirect("/courses/destroy/" + str(id))

def destroy(request, id):
    context = {
        "id": id,
        "name": Course.objects.get(id=id).name,
        "desc": Course.objects.get(id=id).description
    }
    return render(request, "destroy.html", context)

def destroyCourse(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect("/courses")

def back(request):
    return redirect("/courses")