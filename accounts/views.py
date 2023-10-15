from django.shortcuts import render
from . import forms

def home(request):
  return render(
    request, 'accounts/home.html'
  )

def regist(request):
  regist_form = forms.RegistForm(request.POST)
