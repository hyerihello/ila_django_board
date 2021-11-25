from django.contrib.auth.hashers import check_password

from django import forms
from .models import BoardMember

class LoginForm(forms.Form):

    # 입력받을 값 두개
    username = forms.CharField(
        error_messages={'required':'아이디를 입력하세요!'},
        max_length=100, label="사용자이름")
    password = forms.CharField(
        error_messages={'required':'비밀번호를 입력하세요!'},
        widget=forms.PasswordInput, max_length=100, label="비밀번호")
    
    # ---- 클린함수 : 이는 이미 정의되있는 메소드인데, 이게 이미 수행되고 있는 값이 비어있는지(clean) 검사하는 메소드이다.
    def clean(self):
        cleaned_data = super().clean()
        # 처음 값이 들어왔다 는 검증 진행
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        # cleaned_data 의 첫 검증이 끝난 데이터에서 이제 값이 들어있나 확인
        if username and password:
            try:
                member = BoardMember.objects.get(username=username)
            except BoardMember.DoesNotExist:
                self.add_error('username', '아이디가 없습니다!')
                return
                # 예외 처리 후 return을 실행시켜 빠져나오게 한다.
                    
            # 세션처리는 views 내 login 함수에서! 검증만 한다.
            # 위에 (forms.py) from django.contrib.auth.hashers import check_password 입력
            if not check_password(password, member.password):
                self.add_error('password', '비밀번호가 다릅니다!')
            else:
                self.user_id = member.id
