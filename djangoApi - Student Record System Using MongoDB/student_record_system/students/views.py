from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def list(self, request):
        pass

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
