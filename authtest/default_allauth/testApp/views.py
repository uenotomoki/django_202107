#cd django202107/authtest/default_allauth
#python manage.py runserver


from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import Max
#from django.contrib.auth.decorators import login_required
#from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from .models import SnsMessageModel,SnsCommentModel
from .forms import SnsMessageForm,SnsCommentForm

class TopView(TemplateView):
    def __init__(self):
        self.params = {
            'user':'',
            'data':'',
            'data_user':'',
            'data_comment_num':[],
        }

    #@login_required
    def get(self,request):
        if not request.user.is_active:
            return redirect('/accounts/login/')

        user = request.user
        self.params['data'] = SnsMessageModel.objects.all()
        self.params['data_user'] = User.objects.all()

        for i in range(SnsMessageModel.objects.aggregate(Max('id'))['id__max'] + 1):
            if SnsMessageModel.objects.filter(id=i).count() != 0:
                snsmessagemodel_id = SnsMessageModel.objects.filter(id=i)
                print(snsmessagemodel_id)
                self.params['data_comment_num'].append(SnsCommentModel.objects.filter(snsmessagemodel_id = snsmessagemodel_id[0]).count())

        self.params['user'] = user
        return render(request,'testApp/home.html',self.params)

class MySnsShowView(TemplateView):
    def __init__(self):
        self.params = {
            'user':'',
            'data':'',
        }

    #@login_required
    def get(self,request):
        if not request.user.is_active:
            return redirect('/accounts/login/')

        user = request.user
        self.params['data'] = SnsMessageModel.objects.filter(user_id=request.user.id)
        self.params['user'] = user
        return render(request,'testApp/mysnsshow.html',self.params)

class SnsCommentView(TemplateView):
    def __init__(self):
        self.params = {
            'user':'',
            'form':SnsCommentForm(),
            'data':'',
        }

    #@login_required
    def get(self,request,num):
        if not request.user.is_active:
            return redirect('/accounts/login/')

        self.params['data'] = SnsMessageModel.objects.get(id=num)
        self.params['data_user'] = User.objects.get(id=self.params['data'].user_id)
        return render(request,'testApp/snscommentcreate.html',self.params)

    def post(self,request,num):
        if not request.user.is_active:
            return redirect('/accounts/login/')
        
        snsmessagemodel_id = SnsMessageModel.objects.get(id=num)
        message = request.POST['message']
        snscreate = SnsCommentModel(snsmessagemodel_id = snsmessagemodel_id,message = message)
        snscreate.save()
        return render(request,'testApp/mysnsshow.html',self.params)

class SnsCommentIndex(TemplateView):
    def __init__(self):
        self.params = {
            'user':'',
            'form':SnsCommentForm(),
            'data_message':'',
            'data_comment':'',
            'num':''
        }

    #@login_required
    def get(self,request,num):
        if not request.user.is_active:
            return redirect('/accounts/login/')

        self.params['num'] = num
        self.params['data_message'] = SnsMessageModel.objects.get(id=num)
        self.params['data_comment'] = SnsCommentModel.objects.filter(snsmessagemodel_id=self.params['data_message'])
        self.params['data_user'] = User.objects.get(id=self.params['data_message'].user_id)
        return render(request,'testApp/snscommentindex.html',self.params)

    def post(self,request,num):
        if not request.user.is_active:
            return redirect('/accounts/login/')
        
        self.params['num'] = num
        self.params['data_message'] = SnsMessageModel.objects.get(id=num)
        search = request.POST['search']
        self.params['data_comment'] = SnsCommentModel.objects.filter(snsmessagemodel_id=self.params['data_message']).filter(message__icontains=search)
        self.params['data_user'] = User.objects.get(id=self.params['data_message'].user_id)
        return render(request,'testApp/snscommentindex.html',self.params)
        #return render(request,'testApp/snscommentindex.html',{'num': num},self.params)
        #return redirect('snscommentindex',num = num)

class SnsCreateView(TemplateView):
    def __init__(self):
        self.params = {
            'user':'',
            'form':SnsMessageForm(),
            'data':'',
        }

    #@login_required
    def get(self,request):
        if not request.user.is_active:
            return redirect('/accounts/login/')
        return render(request,'testApp/snscreate.html',self.params)

    def post(self,request):
        if not request.user.is_active:
            return redirect('/accounts/login/')
        
        user_id = request.user.id
        message = request.POST['message']
        snscreate = SnsMessageModel(user_id = user_id,message = message)
        snscreate.save()

        return render(request,'testApp/mysnsshow.html',self.params)

class SnsDeleteView(TemplateView):
    def __init__(self):
        self.params = {
            'data':'',
        }
    def get(self,request,num):
        self.params['data'] = SnsMessageModel.objects.get(id=num)
        return render(request,'testApp/snsdelete.html',self.params)
    
    def post(self,request,num):
        data = SnsMessageModel.objects.get(id=num)
        data.delete()
        return redirect('/testApp/snscreate')
