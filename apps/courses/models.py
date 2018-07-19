from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def validator(self, postData):
        errors = {}

        if len(postData["name"]) < 5:
            errors["name"] = "Course name must be 5+ characters long"

        return errors

class DescriptionManager(models.Manager):
    def validator(self, postData):
        errors= {}

        if len(postData["content"]) < 15:
            errors["content"] = "Description must be 15+ characters long"

        return errors

class Course(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    objects = CourseManager()

class Description(models.Model):
    id = models.IntegerField(primary_key=True)
    content = models.TextField()
    course = models.OneToOneField(Course, related_name="desc")

    objects = DescriptionManager()