import mongoengine

# Create your models here.


class Student(mongoengine.Document):
    name = mongoengine.StringField(required=True)
    email = mongoengine.StringField(required=True, unique=True)
    phone = mongoengine.StringField(required=True, unique=True)
    roll_number = mongoengine.IntField(required=True, unique=True)
    date_of_birth = mongoengine.DateTimeField(required=True)
    date_of_joining = mongoengine.DateTimeField(required=True)
    marks = mongoengine.IntField(required=True, min_value=0, max_value=100)
    address = mongoengine.StringField(required=True)
    course = mongoengine.StringField(required=True)
    status = mongoengine.StringField(required=True)
    is_active = mongoengine.BooleanField(default=True)

    def __str__(self):
        return self.name
