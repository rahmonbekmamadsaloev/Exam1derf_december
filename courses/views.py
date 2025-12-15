from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser
from .models import Course, CourseModule, Task
from .serializer import CourseSerializer, CourseModuleSerializer, TaskSerializer

# -=-=-=-= Курсы =-=-=-=
class CourseListCreateAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]  

    def post(self, request, *args, **kwargs):
        self.permission_classes = [IsAdminUser] 
        return super().post(request, *args, **kwargs)

class CourseDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def put(self, request, *args, **kwargs):
        self.permission_classes = [IsAdminUser]
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        self.permission_classes = [IsAdminUser]
        return super().patch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.permission_classes = [IsAdminUser]
        return super().delete(request, *args, **kwargs)

# -=-=- Модули -=-=-=
class CourseModuleListAPIView(generics.ListAPIView):
    queryset = CourseModule.objects.all()
    serializer_class = CourseModuleSerializer
    permission_classes = [AllowAny]

class CourseModuleCreateAPIView(generics.CreateAPIView):
    queryset = CourseModule.objects.all()
    serializer_class = CourseModuleSerializer
    permission_classes = [IsAdminUser]

# =-=-=-=-= Задачи -=-=-=
class TaskListAPIView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Task.objects.all()
        module_id = self.request.query_params.get('module')
        course_id = self.request.query_params.get('course')
        if module_id:
            queryset = queryset.filter(module_id=module_id)
        if course_id:
            queryset = queryset.filter(module__course_id=course_id)
        return queryset

class TaskCreateAPIView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAdminUser]

class TaskDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]

    def put(self, request, *args, **kwargs):
        self.permission_classes = [IsAdminUser]
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        self.permission_classes = [IsAdminUser]
        return super().patch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.permission_classes = [IsAdminUser]
        return super().delete(request, *args, **kwargs)
