from django.urls import path
from .views import (CourseListCreateAPIView,CourseDetailAPIView,CourseModuleListAPIView,CourseModuleCreateAPIView,TaskListAPIView,TaskCreateAPIView,TaskDetailAPIView)

urlpatterns = [
    # =-=-= Курсы -=-=-=
    path('courses/', CourseListCreateAPIView.as_view()),
    path('courses/<int:pk>/', CourseDetailAPIView.as_view()),

    # -=-= Модули -=-=
    path('modules/', CourseModuleListAPIView.as_view()),
    path('modules/create/', CourseModuleCreateAPIView.as_view()),

    # =-=-= Задачи =-=-=-=
    path('tasks/', TaskListAPIView.as_view()),
    path('tasks/create/', TaskCreateAPIView.as_view()),
    path('tasks/<int:pk>/', TaskDetailAPIView.as_view()),
]
