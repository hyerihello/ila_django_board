# :: 장고에서 View 는 다른 MVC 프레임워크에서 말하는 Controller와 비슷한 역할을 한다
# -- 즉, View는 필요한 데이터를 모델(또는 외부)에서 가져와서 적절히 가공후 웹 페이지 결과를 만들도록 컨트롤 하는 역할

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password

from .models import BoardMember
from .forms import LoginForm
# class BoardMember(models.Model):


# --  1. 클라이언트가 요청하는(웹페이지를 보여줘, 회원가입을 시켜줘 등) 요청정보가 request라는 변수를 통해 들어온다
# --  2. render는 request요청을 전달 해 주고 동시에 반환해 주고자 하는 html파일도 인자에 담아 리턴해준다
def home(request):
    return render(request, 'home.html')
    """
    user_id = request.session.get('user')
     if user_id:
        member = BoardMember.objects.get(pk=user_id)
        # 아까 세션에 id 를 넣어놓았었다. 세션의 user 키에 넣어 두었던게 id 값이였다.
        return HttpResponse(member.username)
    # 아! 로그인을 안했을 때!, user_id 가 없을 때? (세션이 만료되었을 때?)
    return HttpResponse('Home!')"""
    # 로그인을 안했을 때 '/' 로 리다이렉트 되면서 'Home!' 문구가 뜰 것이다.


'''
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')

    elif request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        res_data ={}
        if not (username and password):
            res_data['error'] = '모든 값을 입력하세요!'

        else:
            member = BoardMember.objects.get(username=username)
            #print(member.id)

            if check_password(password, member.password):
                #print(request.session.get('user'))
                # 세션에서 user를 key로 하고 할당받은 member.id로 설정, 나중에 쿠키에 저장됨
                request.session['user'] = member.id

                return redirect('/')


            else:
                res_data['error'] = '비밀번호가 다릅니다!'

        return render(request, 'login.html', res_data) 
'''


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        # 폼 객체, 폼 클래스를 만들 때 괄호에 POST 데이터를 담아준다.
        # POST 안에 있는 데이터가 form 변수에 들어간다.
        if form.is_valid(): # 장고 폼에서 제공하는 검증 함수 is_valid()
            # session_code 검증하기
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form = LoginForm()
        # 빈 클래스 변수를 만든다.
    return render(request, 'login.html', {'form':form})





def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/')




def register(request):
    if request.method == "GET":
        return render(request, 'register.html')

    elif request.method == "POST":
        #print (request.POST)
        username    = request.POST.get('username', None)
        #print(username)
        password    = request.POST.get('password', None)
        #print(password)
        re_password = request.POST.get('re_password', None)
        #print(re_password)
        email       = request.POST.get('email', None)


        res_data = {}
        if not (username and password and re_password and email):
            res_data['error'] = '모든 값을 입력하세요!'

        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다'
            print(res_data)
        
        else:
        # ---- 왼쪽 username :: 변수
	    # ---- 오른쪽 username = request.POST['username']의 username
            member = BoardMember(
                username    = username,
                email       = email,
                password    = make_password(password)
            )
            member.save() # db저장

        return render(request, 'register.html', res_data)
        #print(res_data)