from django.shortcuts import render
from django.http import HttpResponse
from twitter.forms import TwitterForm

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def twitter_graph(request):
    if request.method == 'POST':
        form = TwitterForm(request.POST)
        if form.is_valid():
            #return HttpResponseRedirect('/thanks/')
            print("valid")
        else:
            form = TwitterForm()
    print("prueba")
    form = TwitterForm()
    return render(request, 'twitter.html', {'form': form})
    