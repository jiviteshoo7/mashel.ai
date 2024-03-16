from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'), 
    path('mashel_ai/', views.mashel_ai, name='mashel_ai'),
    path('chatbot/', views.chatbot, name='chatbot'), 
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()
