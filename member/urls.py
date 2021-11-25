from django.urls import path
from . import views

# 멤버의 회원가입 경로는 http://127.0.0.1:8000/member/register 가 되고, 
# 이 경로에서 아까 views.py 에 작성했던 함수 register 를 실행하게 한다.
# from . import views로 불러오게 한다. 이제 def register() 함수가 실행되면서 html화면을 불러오게 된다.
urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout),
]