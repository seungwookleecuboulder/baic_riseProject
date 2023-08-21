"""
URL configuration for baic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from django.contrib import admin
from django.urls import path
from rise.views import subject_list, subject_new, subject_delete, subject_update, subject_download, subject_upload, subject_statics, subject_statics_download,\
    poverty_list, poverty_download, poverty_upload, poverty_delete, \
    interview_list, interview_new, interview_update, interview_delete, interview_download, interview_upload

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', subject_list, name='home'),

    path('subjectList/', subject_list, name='subject_list'),
    path('subjectNew/', subject_new, name='subject_new'),
    path('subjectUpdate/<str:subject_id>', subject_update, name='subject_update'),
    path('subjectDelete/<str:subject_id>', subject_delete, name='subject_delete'),
    path('subjectDownload/', subject_download, name='subject_download'),
    path('subjectUpload/', subject_upload, name='subject_upload'),
    path('subjectStatics/<str:subject_id>', subject_statics, name='subject_statics'),
    path('subjectStaticsDownload/', subject_statics_download, name='subject_statics_download'),

    path('povertyList/', poverty_list, name='poverty_list'),
    path('povertyDownload/', poverty_download, name='poverty_download'),
    path('povertyUpload/', poverty_upload, name='poverty_upload'),
    path('povertyDelete/<int:year>', poverty_delete, name='poverty_delete'),

    path('interviewList/', interview_list, name='interview_list'),
    path('interviewNew/', interview_new, name='interview_new'),
    path('interviewNew/<str:interview_id>', interview_new, name='interview_new'),
    path('interviewUpdate/<str:interview_id>', interview_update, name='interview_update'),
    path('interviewDelete/<str:interview_id>', interview_delete, name='interview_delete'),
    path('interviewDownload/', interview_download, name='interview_download'),
    path('interviewUpload/', interview_upload, name='interview_upload'),

]

