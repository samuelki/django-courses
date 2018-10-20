from django.db import models

class CourseManager(models.Manager):
    def validate_form(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors['name'] = "Course name should be more than 5 characters."
        if len(postData['description']) < 15:
            errors['description'] = "Course description should be more than 15 characters."
        return errors

class CommentManager(models.Manager):
    def validate_comment_form(self, postData):
        errors = {}
        if len(postData['comment']) > 254:
            errors['comment'] = "Comment is too long."
        return errors

class Description(models.Model):
    description = models.TextField()

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.OneToOneField(Description)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CourseManager()

class Comment(models.Model):
    name = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
    course = models.ForeignKey(Course, related_name="comments")

    objects = CommentManager()