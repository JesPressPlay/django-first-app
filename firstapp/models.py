from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Note: __str__ is added to each model to improve admin experience. It decides how
# an object is labeled in the admin dropdowns and lists. Much better for when assigning objects.

# One-to-One relationship. Instructor links to exactly one User.
class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # When the parent dissapears, delete the User and its Instructor row too.
    full_time = models.BooleanField(default=True)
    total_learners = models.IntegerField()

    def __str__(self):
        return self.user.username

# Many-to-Many relationship
class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    pub_date = models.DateField(null=True)
    instructors = models.ManyToManyField(Instructor)
    total_enrollment = models.IntegerField(default=0)

    def __str__(self):
        return self.name

# Many-to-one relationship
class Lesson(models.Model):
    title = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title