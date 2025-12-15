from django.urls import path
from .views import SubmissionListCreateAPIView, SubmissionDetailAPIView

urlpatterns = [
    path('submissions/', SubmissionListCreateAPIView.as_view()),
    path('submissions/<int:pk>/', SubmissionDetailAPIView.as_view()),
]
