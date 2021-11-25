from django.http.response import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from member.models import BoardMember
from .models import Board
from .forms import BoardForm



def board_list(request):
    # 변수 명을 all_board 로 변경
    all_boards= Board.objects.all().order_by('-id') # 역순으로 최신사항을 먼저 보이게 가져오겠다는 코드 
    # p 라는 값으로 받고, 없으면 첫번째 페이지로 
    page = int(request.GET.get('p',1))
    # Paginator 함수를 적용하는데, 첫번째 인자는 위에 변수인 전체 오브젝트, 2번째 인자는
    # 한 페이지당 오브젝트 2개씩 나오게 설정
    pagenator = Paginator(all_boards, 2)
    # 처음 2개 셋팅 
    boards = pagenator.get_page(page)
    return render(request, 'board_list.html', {"boards":boards})



def board_write(request):
    if not request.session.get('user'):
        return redirect('/member/login/')
        # session 에 'user' 키를 불러올 수 없으면, 로그인 하지 않는 사용자 이므로 로그인 페이지로 리다이렉트함

    if request.method == "POST":
        form = BoardForm(request.POST)

        if form.is_valid():
            # form의 모든 validators 호출 유효성 검증 수행
            user_id = request.session.get('user')
            member = BoardMember.objects.get(pk=user_id)
            
            board = Board()
            board.title     = form.cleaned_data['title']
            board.contents  = form.cleaned_data['contents']
            # 검증에 성공한 값들은 사전타입으로 제공 (form.cleaned_data)
            # 검증에 실패시 form.error 에 오류 정보를 저장
            
            board.writer    = member
            board.save() # db에 저장 

            # 저장 후 목록으로 리다이렉트 해야함
            return redirect('/board/list/')

    else:
        form = BoardForm()

    return render(request, 'board_write.html', {'form': form})




def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다.')
        # 게시물 내용을 찾을 수 없을 때 오류 메세지 :: 상단에 from django.http import Http404 

    # pk 에 해당하는 글을 가지고 올 수 있게 된다.
    return render(request, 'board_detail.html', {'board':board})
    # {'board':board} 로 템플릿에 전달해 준다.

    