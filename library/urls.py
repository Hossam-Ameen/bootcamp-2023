"""
URL configuration for library project.

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
from django.urls import path
from student.views_base_function import student_api_view, update_student
from student.views_with_api_class import StudentAPI
from student.views import StudentList, StudentCreation, StudentRetrieve, StudentUpdation, StudentDeletion

urlpatterns = [
    # base function
    path("students/", student_api_view),
    path("students/<int:id>/", update_student),
    # APIView class
    # path("students/", StudentAPI.as_view()),
    # path("students/<int:pk>/", StudentAPI.as_view()),
    # GenericAPIView
    # path('students/', StudentList.as_view()),
    # path('create-students/', StudentCreation.as_view()),
    # path('retrieve-students/<int:pk>/', StudentRetrieve.as_view()),
    # path('update-students/<int:pk>/', StudentUpdation.as_view()),
    # path('delete-students/<int:pk>/', StudentDeletion.as_view())
]
