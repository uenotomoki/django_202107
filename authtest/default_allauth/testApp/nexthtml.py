from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import Max
from django.core.paginator import Paginator
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import SnsMessageModel,SnsCommentModel
from .forms import SnsMessageForm,SnsCommentForm

class RenderMysnsshow:
    def __init__(self):
        self.params = {
            'user':'',
            'data':'',
        }

    def rendermysnsshow(self,request):
        user = request.user
        self.params['user'] = user
        self.params['data'] = SnsMessageModel.objects.filter(user_id=user.id).order_by('id').reverse()

        return render(request,'testApp/mysnsshow.html',self.params)