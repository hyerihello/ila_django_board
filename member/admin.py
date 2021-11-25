# 관리자 페이지
from django.contrib import admin
# Register your models here.

# 현재 경로의 models에서 클래스 BoardMember 불러온다
from .models import BoardMember

# BoardMemeberAdmin 클래스를 만들고 괄호안에 인자로 받는것은 
# model.Model과 동일하게 admin에서 ModelAdmin 상속해 온다 라고 이해하면 된다.
class BoardMemberAdmin(admin.ModelAdmin):
    
    # 관리자 페이지에 보이게 하기 
    list_display = ('username', 'email', 'password', 'created_at', 'updated_at')

# 관리자 페이지에 등록하기 
admin.site.register(BoardMember, BoardMemberAdmin)