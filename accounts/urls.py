from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
  # views モジュール内の home 関数が呼び出され、このURLに関連付けられる
  # /dairy_thread → urls.py → accounts/urls.py → accounts/view.py
  path('', views.home, name='home'),
  path('regist', views.regist, name='regist')
]