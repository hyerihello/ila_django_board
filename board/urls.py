from django.urls import path
from . import views

# 'board'/ 아래로 연결되는 경로 중 게시판의 리스트를 보여주는  엔드포인트와 연결 되었을 때 실행되는 함수 
urlpatterns = [
    path('list/', views.board_list),
    path('write/', views.board_write),
    path('detail/<int:pk>/', views.board_detail),
    # -------- edit-update, delete
    path('detail/<int:pk>/delete/',views.delete),
    #path('detail/<int:pk>/edit/', views.edit),
    path('update/<int:pk>/', views.update, name="update"),
]