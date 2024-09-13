import mongoengine

# Create your models here.


class Student(mongoengine.Document):

    def __str__(self):
        return self.name
