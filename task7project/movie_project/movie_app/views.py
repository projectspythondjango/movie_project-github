from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .models import Movie
from .forms import MovieForm

def index(request):
    movie=Movie.objects.all()
    context={'movielist':movie}

    return render(request,"index.html",context)
def detail(request,movieid=id):
    movie=Movie.objects.get(id=movieid)
    return render(request,"detail.html",{'movie':movie})

def add_movies(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc1=request.POST.get('desc')
        year1=request.POST.get('year')
        image1=request.FILES['image']
        movie1=Movie(name=name,desc=desc1,year=year1,image=image1)
        movie1.save()
    return render(request, "add.html")

def update(request,id):
    movie2=Movie.objects.get(id=id)
    form1=MovieForm(request.POST or None,request.FILES,instance=movie2)
    if form1.is_valid():
        form1.save()
        return redirect('/')
    return render(request,"edit.html",{'form':form1,'movie':movie2})
def delete(request,id):
    if request.method=="POST":
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,"delete.html")

