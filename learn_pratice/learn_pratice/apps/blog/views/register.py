# import re
# from django.http import HttpResponse
# from django.shortcuts import render
# from django.contrib.auth import get_user_model
#
# _RE_EMAIL = re.compile(r'^[a-z0-9\.\-\_]+\@[a-z0-9\-\_]+(\.[a-z0-9\-\_]+){1,4}$')
# _RE_SHA1 = re.compile(r'^[0-9a-f]{40}$')
#
#
#
#
#
#
#
# # class LoginView(View):
# #
# #   def get(self,request):
# #     #逻辑代码
# #     return render(request,'login.html')
# #
# #   def post(self,request):
# #     # 获取前端传递过来的用户名和密码
# #     username = request.POST.get('username')
# #     pwd = request.POST.get('pwd')
# #     record = request.POST.get('record')
# #     # 进行数据校验
# #     if not all([username,pwd]):
# #       return HttpResponse('数据输入不完整')
# #     # 验证用户名和密码是否正确
# #     user = authenticate(username=username,password=pwd)
# #     return render(request,''index.html')
#
#
# # pip install django-filer
#
#
# def register(request):
#     print('------------------------')
#     print(request.POST)
#     # 这个方法会从settings中找AUTH_USER_MODEL ,然后取得的User
#     # 至于为何不直接那models里的User  暂时不清楚,后续会去测试,知道后再修改本文
#     user = get_user_model()
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         email = request.POST.get('email')
#         user.photo = '123123'
#         print(user.__str__)
#     return render(request, 'login_register.html')