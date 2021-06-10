
from django.contrib import admin
from django.urls import path

from distributer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/news/', views.NewsListApiView.as_view()),
    path('api/v1/news/<int:id>/', views.NewsDetailApiView.as_view()),
    path('api/v1/laws/', views.LawListApiView.as_view()),
    path('api/v1/law/<int:id>/', views.LawsDetailApiView.as_view()),
    path('api/v1/laws/', views.LawListApiView.as_view()),
    path('api/v1/Publication/', views.PublicationListApiView.as_view()),
    path('api/v1/Publication/<int:id>/', views.PublicationDetailApiView.as_view()),
    path('api/v1/Login/', views.login_View),

]
