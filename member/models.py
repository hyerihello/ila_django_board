from django.db import models

# 모델들은 보통 app의 model.py에서 정의된다 
'''
이들은 django.db.models.Model의 서브클래스로 구현
필드, 메소드, 메타데이터 포함할 수 있다
아래는 "BoardMember라고 이름지어진 모델이다"
'''
# Create your models here.


class BoardMember(models.Model):
    username    = models.CharField(max_length=100, verbose_name='유저ID')
    email       = models.EmailField(max_length=100, verbose_name='유저메일')
    password    = models.CharField(max_length=100, verbose_name='유저PW')
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name='가입날짜')
    updated_at  = models.DateTimeField(auto_now=True, verbose_name='마지막수정일')

    # Methods
    # --- 생성되는 객체 타입을 문자열로 변환해서 보여주게 한다.
    # --- 생성된 객체가 username으로 보기에 한다. 설정을 하지 않았을 시 object(1) 이렇게 표시된다
    def __str__(self):
        return self.username

    # Meta data
    # --- db_dable은 데이터베이스에 저장되는 테이블 명을 의미한다, 보통 클래스명의 복수형으로 표기한다.
    class Meta:
        db_table            = 'boardmembers'
        # --- 사용자가 읽기 쉬운 모델 객체의 이름으로 관리자 화면 등에서 표시, 영어를 기준으로 단수형
        verbose_name        = '게시판멤버' 
        # --- 사용자가 읽기 쉬운 모델 객체의 이름으로 관리자 화면 등에서 표시, 영어를 기준으로 복수형, 
        #     한국에서는 단수 복수를 구별해 사용하지 않으므로 verbose_name과 동일하게 사용
        verbose_name_plural = '게시판멤버'