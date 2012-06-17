# -*- coding: utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from kusskr.apps.blog.models import Article, Comment, Category

def index(request):
    return render_to_response('blog/index.html', {

    }, context_instance=RequestContext(request))

def view_by_category(request, category):
    return render_to_response('blog/index.html', {

    }, context_instance=RequestContext(request))

def view_by_no(reqeust, article_no):
    return render_to_response('blog/view.html', {
    
    }, context_instance=RequestContext(request))

def add_post(request):
    return render_to_response('blog/view.html', {

    }, context_instance=RequestContext(request))

def add_post_form(request):
    return render_to_response('blog/edit.html', {

    }, context_instance=RequestContext(request))

def delete_post(request):
    return render_to_response('blog/index.html', {

    }, context_instance=RequestContext(request))

def add_comment(request):
    return HttpResponse(json.dumps({

    }, ensure_ascii=False, indent=4)

def add_category(request):
    return HttpResponse(json.dumps({

    }, ensure_ascii=False, indent=4)
