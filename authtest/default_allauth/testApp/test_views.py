#python manage.py test

from django.test import TestCase, Client, RequestFactory
from django.urls import reverse

from django.contrib.auth.models import User
from .views import TopView

class IndexTests(TestCase):
  """IndexViewのテストクラス"""

  def setUp(self):
    User.objects.create_user(username='test_account', email='test_account@aaa.bbb', password='test_pass') 

  def test_get(self):
    """ログイン画面へGET メソッドでアクセスしてステータスコード200を返されることを確認"""
    client = Client()
    response = client.get('/accounts/login/')
    self.assertEqual(response.status_code, 200)
  
  def test_login(self):
    self.client = Client()
    self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    self.client.login(username='john', password='johnpassword')
    response = self.client.get('/testApp/snscreate/')
    self.assertEqual(response.status_code, 200)