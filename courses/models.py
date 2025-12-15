from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class CourseModule(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField()

    def __str__(self):
        return self.course.title


class Task(models.Model):
    module = models.ForeignKey(CourseModule,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    max_score = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
