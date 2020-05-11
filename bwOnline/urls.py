from django.urls import path,include,re_path
from django.views.generic.base import TemplateView
from users.views import LoginView,RegisterView,ForgetPwdView,ActiveUserView,ResetView,ModifyPwdView
from django.views.static import serve
from bwOnline.settings import MEDIA_ROOT
import xadmin

urlpatterns = [
    path('xadmin/',xadmin.site.urls),
    path('login/',LoginView.as_view(),name='login'),
    path('',TemplateView.as_view(template_name='index.html'),name='index'),
    path('register/',RegisterView.as_view(),name='register'),
    path('captcha/',include('captcha.urls')),  #验证码路由
    path('forget/',ForgetPwdView.as_view(),name='forget'),
    path('modify_pwd/', ModifyPwdView.as_view(), name='modify_pwd'),
    re_path('active/(?P<active_code>.*)/',ActiveUserView.as_view(),name='user_active'),
    re_path('reset/(?P<active_code>.*)/',ResetView.as_view(),name='reset_pwd'),

    # path('course/',include('course.urls',namespace='course')),
    path("org/", include('organization.urls', namespace="org")),
    # 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT
    re_path(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT })
]
