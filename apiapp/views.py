from django.shortcuts import render
from django.http import JsonResponse

def ask_question(request):
    return JsonResponse({"message": "Hello World"})
