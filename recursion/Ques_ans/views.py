from django.shortcuts import render
from .models import Question

# Create your views here.
def home(request):
    return render(request, 'home.html')


def question(request):
    if request.method == "POST":
        name = request.POST.get('name','')
        question = request.POST.get('question','')
        q = Question(name = name, question = question)
        q.save()
    return render(request, 'question.html')


