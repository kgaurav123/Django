from django.shortcuts import render
from .models import question

# Create your views here.
def home(request):
    return render(request, 'home.html')


def question(request):
    if request.method == "POST":
        name = request.POST.get('name','')
        question = request.POST.get('question','')
        q = question(name=name, question=question)
        q.save()
    return render(request, 'question.html')


