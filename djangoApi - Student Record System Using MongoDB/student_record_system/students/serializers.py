from rest_framework_mongoengine.serializers import DocumentSerializer
from .models import Student


class StudentSerializer(DocumentSerializer):
    class Meta:
        model = Student
        managed = False
        fields = '__all__'  # All fields will be serialized
