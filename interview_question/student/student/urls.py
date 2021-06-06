"""student URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from app import views
router = routers.DefaultRouter()
router.register(r'student_login', views.student_login,basename='student_login')
router.register(r'student_register',views.studentRegister,basename='student_register')
router.register(r'student_score',views.TestScore,basename='student_score')
router.register(r'highest_score_AvgScore',views.highest_score_AvgScore,basename='highest_score_AvgScore')
router.register(r'all_candidate',views.show_all_candidate,basename="all_candidate")

urlpatterns = [


    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
