#!/usr/bin/env python  
# encoding: utf-8   

""" 
@version: v1.0 
@author: Lomedy
@license: Apache Licence  
@contact: 284241181@qq.com 
@software: PyCharm 
@file: forms.py 
@time: 2018/1/28 0028 16:20 
"""

from django import forms

class CommnetForm(forms.Form):
    '''
    评论表单用于发表博客的评论
    '''
    name = forms.CharField(label='称呼',max_length=16,error_messages={
        'required':'请填写您的称呼',
        'max_length':'称呼太长',
    })
    email = forms.EmailField(label='邮箱',error_messages={
        'required':'请填写您的邮箱',
        'invalid':'邮箱格式不正确',
    })

    content = forms.CharField(label='评论内容',error_messages={
        'required':'请填写您的评论内容',
        'max_length':'评论内容太长'
    })