from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(reqeust):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(reqeust, question_id):
    HttpResponse = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(reqeust, question_id):
    return HttpResponse("You're voitng on quesiton %s." % question_id)
