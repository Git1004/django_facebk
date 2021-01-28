from django.shortcuts import render


# Create your views here.
def play(request):
    return render(request, 'play.html')


# def play2(request):
#     testguy='테스트가이'
#     return render(request, 'play2.html',{ 'name': testguy})

# count = 0
# def play2(request):
#     choidogeun = '최도근'
#     age = 20
#     global count  # 바깥영역의 변수를 사용할 때 global
#     count = count + 1  # 접속할 때마다 방문자 1 증가
#
#     if age > 19:  # age가 19 보다 크면?
#         status = '성인'
#     else:  # 성인이 아닌 경우
#         status = '청소년'
#
#     return render(request, 'play2.html', {'name': choidogeun, 'cnt': count, 'age': status})


count = 0


def play2(request):
    choidogeun = '최도근'
    age = 10

    global count  # 바깥영역의 변수를 사용할 때 global
    count = count + 1  # 접속할 때마다 방문자 1 증가

    if age > 19:  # age가 19 보다 크면?
        status = '성인'
    else:  # 성인이 아닌 경우
        status = '청소년'

    diary = ['오늘은 날씨가 맑았다. - 4월 3일', '미세머지가 너무 심하다. (4월 2일)', '비가 온다. 4월 1일에 작성']

    # if count % 7 == 0 :
    if count % 7 is 0:
        victory = '7배수 방문 이벤트!! 당첨되셨어요'
    else:
        victory = '꽝'
    return render(request, 'play2.html',
                  {'name': choidogeun, 'diary': diary, 'cnt': count, 'age': status, 'victory': victory})


def profile(request):
    return render(request, 'profile.html')


# def newsfeed(request):
#     return render(request, 'newsfeed.html')

from django.shortcuts import render
from facebook.models import Article
from facebook.models import Page


def newsfeed(request):
    articles = Article.objects.all()
    return render(request, 'newsfeed.html', {'articles': articles})


def detail_feed(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'detail_feed.html', {'feed': article})


def pages(request):
    pages = Page.objects.all()
    return render(request, 'page_list.html', {'pages': pages})


from django.shortcuts import redirect


def new_feed(request):
    if request.method == 'POST':  # 폼이 전송되었을 때만 아래 코드를 실행
        if request.POST['author'] != '' and request.POST['title'] != '' and request.POST['content'] != '' and \
                request.POST['password'] != '':
            new_article = Article.objects.create(
                author=request.POST['author'],
                title=request.POST['title'],
                text=request.POST['content'],
                password=request.POST['password']
            )

            # 새글 등록 끝
            return redirect(f'/feed/{new_article.pk}')
            # 변수를 따옴표 안에 넣으려면 맨앞에 f 를 붙이고 중괄호 {} 안에 입력한다.
        else:
            print('글을 입력하세요')
    return render(request, 'new_feed.html')

#
# def edit_feed(request, pk):
#     article = Article.objects.get(pk=pk)
#
#     if request.method == 'POST':
#         article.author = request.POST['author']
#         article.title = request.POST['title']
#         article.text = request.POST['content']
#         article.save()
#         return redirect(f'/feed/{article.pk}')
#
#     return render(request, 'edit_feed.html', {'feed': article})


# def remove_feed(request, pk):
#     article = Article.objects.get(pk=pk)
#
#     if request.method == 'POST':
#         if request.POST['password'] == article.password:
#             article.delete()
#             return redirect('/')  # 첫페이지로 이동하기
#
#     return render(request, 'remove_feed.html', {'feed': article})


# def remove_feed(request, pk):
#     return render(request, 'remove_feed.html')

def remove_feed(request, pk):
    article = Article.objects.get(pk=pk)
    print(pk, '삭제페이지.')
    # return render(request, 'remove_feed.html', {'feed': article})
    if request.method == 'POST':
        if request.POST['password'] == article.password:
            article.delete()
            return redirect('/')  # 첫페이지로 이동하기

        else:
            return redirect('/fail/')  # 비밀번호 오류 페이지 이동하기

    return render(request, 'remove_feed.html', {'feed': article})


def edit_feed(request, pk):
    article = Article.objects.get(pk=pk)
    print(pk, '수정페이지.')
    if request.method == 'POST':
        if request.POST['password'] == article.password:
            article.author = request.POST['author']
            article.title = request.POST['title']
            article.text = request.POST['content']
            article.save()
            return redirect(f'/feed/{article.pk}')
        else:
            return redirect('/fail/')  # 비밀번호 오류 페이지 이동하기

    return render(request, 'edit_feed.html', {'feed': article})


def fail(request):
    return render(request, 'fail.html')


def new_page(request):
    if request.method == 'POST':
        new_page = Page.objects.create(
            master=request.POST['master'],
            name=request.POST['name'],
            text=request.POST['text'],
            category=request.POST['category']
        )

        # 새 페이지 개설 완료
        return redirect('/pages/')

    return render(request, 'new_page.html')



def remove_page(request, pk):
    page = Page.objects.get(pk=pk)

    if request.method == 'POST':
        page.delete()
        return redirect('/pages/')

    return render(request, 'remove_page.html', {'page': page})

def edit_page(request, pk):
    page = Page.objects.get(pk=pk)

    if request.method == 'POST':
        page.master = request.POST['master']
        page.name = request.POST['name']
        page.text = request.POST['text']
        page.category = request.POST['category']
        page.save()
        return redirect('/pages/')

    return render(request, 'edit_page.html', {'page': page })




from facebook.models import Comment

def detail_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':  # new comment
        Comment.objects.create(
            article=article,
            author=request.POST.get('nickname'),
            text=request.POST.get('reply'),
            password=request.POST.get('password')
        )

        return redirect(f'/feed/{ article.pk }')

    return render(request, 'detail_feed.html', {'feed': article})