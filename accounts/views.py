from django.shortcuts import render
from . import forms

def home(request):
  return render(
    request, 'accounts/home.html'
  )

def regist(request):
  regist_form = forms.RegistForm(request.POST)
  
  if regist_form.is_valid():
    regist_form.save()

    return render(
      request, 'accounts/regist.html', context={
        'regist_form': regist_form
      }
    )
