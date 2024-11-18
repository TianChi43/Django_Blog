import markdown
# 导入数据模型ArticlePost
from .models import ArticlePost
# 引入redirect重定向模块
from django.shortcuts import render, redirect
# 引入HttpResponse
from django.http import HttpResponse
# 引入刚才定义的ArticlePostForm表单类
from .forms import ArticlePostForm
# 引入User模型
from django.contrib.auth.models import User


def article_list(request):
    # 取出所有博客文章
    articles = ArticlePost.objects.all()
    # 需要传递给模板（templates）的对象
    context = {'articles': articles}
    # render函数：载入模板，并返回context对象
    return render(request, 'article/list.html', context)


def article_detail(request, id):
    # 取出相应的文章
    article = ArticlePost.objects.get(id=id)
    article.body = markdown.markdown(article.body,
                                     extensions=[
                                         # 包含 缩写、表格等常用扩展
                                         'markdown.extensions.extra',
                                         # 语法高亮扩展
                                         'markdown.extensions.codehilite',
                                     ])

    # 需要传递给模板的对象
    context = {'article': article}
    # 载入模板 并返回context对象
    return render(request, 'article/detail.html', context)


def article_create(request):
    # 判断用户是否提交数据
    if request.method == 'POST':
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            new_article = article_post_form.save(commit=False)
            # 指定目前登录的用户作为作者
            new_article.author = User.objects.get(id=request.user.id)
            new_article.save()
            return redirect("article:article-list")
        else:
            return HttpResponse("表单内容有误，请重新填写")
    else:
        # 创建表单类实例
        article_post_form = ArticlePostForm()
        # 赋值上下文
        context = {'article_post_form': article_post_form}
        # 返回模板
        return render(request, 'article/create.html', context)


def article_delete(request, id):
    article = ArticlePost.objects.get(id=id)
    article.delete()
    return redirect("article:article-list")


# 安全删除文章
def article_safe_delete(request, id):
    article = ArticlePost.objects.get(id=id)
    if request.method == 'POST':
        if request.user != article.author:
            return HttpResponse("你没有权限删除这篇博客。")
        article = ArticlePost.objects.get(id=id)
        article.delete()
        return redirect("article:article-list")
    else:
        return HttpResponse("仅允许post请求")


# 更新文章
def article_update(request, id):
    article = ArticlePost.objects.get(id=id)
    if request.method == "POST":
        if request.user != article.author:
            return HttpResponse("你没有权限修改这篇博客。")
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            article.body = request.POST['body']
            article.title = request.POST['title']
            article.save()
            return redirect("article:article-detail", id=id)
        else:
            return HttpResponse("表单内容有误，请重新填写")

    else:
        article_post_form = ArticlePostForm()
        context = {'article_post_form': article_post_form, 'article': article}
        return render(request, 'article/update.html', context)
