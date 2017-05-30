from django.shortcuts import render, redirect

from .models import Book
def index(request):
    context = {
    "books" : Book.objects.all()
    }
    return render(request, 'fullstack_books_app/index.html', context)

def create(request):
    postData = {
    'title' : request.POST['title'],
    'author' : request.POST['author'],
    'category' : request.POST['category']
    }

    model_resp = Book.objects.title_must_not_be_blank(postData)
    print model_resp

    if model_resp[0] == True:
        print "Book successfully created!"
    else:
        print "You know you done fucked up right?"

    return redirect('/')
# Create your views here.
