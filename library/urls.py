from django.urls import path
from student.views import StudentViewSet, UserLoginView

urlpatterns = [
    path('students/',   StudentViewSet.as_view({
             'get': 'list',
             'post': 'create'
         })),
    path('students/<int:pk>/', StudentViewSet.as_view({
             'get': 'retrieve',
             'put': 'update',
             'patch': 'partial_update',
             'delete': 'destroy'
         })),
    path('login/', UserLoginView.as_view(), name='user-login'),

]
