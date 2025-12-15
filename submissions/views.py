from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Submission
from .serializer import SubmissionSerializer
from .paginations import Paginations

# =-=-=-= Список и создание -=-=-==
class SubmissionListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = SubmissionSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = Paginations

    def get_queryset(self):
        if self.request.user.is_staff:
            return Submission.objects.all()
        return Submission.objects.filter(user=self.request.user)


class SubmissionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SubmissionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Submission.objects.all()
        return Submission.objects.filter(user=self.request.user)
