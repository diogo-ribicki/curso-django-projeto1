from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse

class HomeView(TemplateView):
    def get(self, request, *args, **kwargs):
        data = 'Hello world!'
        return JsonResponse({'message': data})