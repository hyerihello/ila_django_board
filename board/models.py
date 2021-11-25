from django.db import models

# Create your models here.


class Board(models.Model):
    title       = models.CharField(max_length=200, verbose_name="제목")
    contents    = models.TextField(verbose_name="내용")
    # 게시물과 멤버의 관계가 외래키로 연결, 
    # -- on_delete 조건은 회원가입 한 사용자가 삭제되면 그 사용자가 작성한 게시글도 모두 지우겠다는 의미 
    writer      = models.ForeignKey('member.BoardMember', on_delete=models.CASCADE, verbose_name="작성자")
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name="작성일")
    updated_at  = models.DateTimeField(auto_now=True, verbose_name="최종수정일")

    def __str__(self):
        return self.title

    class Meta:
        db_table            = 'boards'
        verbose_name        = '게시판'
        verbose_name_plural = '게시판'

