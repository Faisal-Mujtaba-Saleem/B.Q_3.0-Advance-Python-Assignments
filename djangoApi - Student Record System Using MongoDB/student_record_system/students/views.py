from rest_framework import viewsets, status, exceptions
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def list(self, request):
        """Endpoint: GET /api/students/"""

        try:
            student_record = self.get_queryset()
            student_serializer = self.get_serializer(student_record, many=True)
            return Response(student_serializer.data, status=status.HTTP_200_OK)

        except exceptions.NotFound:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            print(e)
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        """Endpoint: POST /api/students/"""

        try:
            data = request.data
            student_serializer = self.get_serializer(data=data)

            if student_serializer.is_valid():
                student_serializer.save()
                return Response(data=data, status=status.HTTP_201_CREATED)

            return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except exceptions.NotFound:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Endpoint: GET /api/students/:id/"""

        try:
            student = self.get_object()
            student_serializer = self.get_serializer(student)

            return Response(student_serializer.data, status=status.HTTP_200_OK)

        except exceptions.NotFound:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        """Endpoint: PUT /api/students/:id/"""

        try:
            student = self.get_object()
            student_serializer = self.get_serializer(
                student, request.data, partial=True
            )

            if student_serializer.is_valid():
                student_serializer.save()
                return Response(student_serializer.data, status=status.HTTP_200_OK)

            return Response(student_serializer.errors, status=status.HTTP_404_NOT_FOUND)

        except exceptions.NotFound:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """Endpoint: DELETE /api/students/:id/"""

        try:
            student = self.get_object()
            self.perform_destroy(student)

            return Response(status=status.HTTP_204_NO_CONTENT)

        except exceptions.NotFound:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
