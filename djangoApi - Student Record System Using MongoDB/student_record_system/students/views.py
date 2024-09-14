from rest_framework import viewsets, status, exceptions
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

# viewset for student


class StudentViewSet(viewsets.ModelViewSet):
    # Initializing the queryset and defining the serializer class. queryset is a set of objects to be serialized present in the particular collection of a database & serializer_class is used to manage the serialization & Schema of the data.
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def list(self, request):
        """Endpoint: GET /api/students/"""

        try:
            # Fetching the queryset through get_queryset() method returnscontaining all the records in the collection and serializing it using get_serializer() method.

            # get_serializer() method uses the serializer_class to serialize the querysets/db model instances into python native data structures deserialize the python native data structures into querysets/db model instances and validate them according to the schema defined in serializer_class on calling is_valid() method on the deserialized data.

            student_record = self.get_queryset()
            student_serializer = self.get_serializer(student_record, many=True)

            # Returning the serialized data along with status code 200

            return Response(student_serializer.data, status=status.HTTP_200_OK)

        # Handling exceptions

        # Handling exception if the record is not found

        except exceptions.NotFound:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        # Handling general exceptions

        except Exception as e:
            print(e)
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        """Endpoint: POST /api/students/"""

        try:
            # Fetching the data from the request, i.e. user has posted and de-serializing it using get_serializer() method.

            data = request.data
            student_serializer = self.get_serializer(data=data)

            # Checking the data if it is valid/de-serialized according to schema of the serializer_class

            if student_serializer.is_valid():

                # Saving the data into the database

                student_serializer.save()

                # Returning the saved data along with status code 201
                return Response(data=data, status=status.HTTP_201_CREATED)

            # Returning the errors if the data is not valid

            return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Handling exceptions

        # Handling exception if the record is not found

        except exceptions.NotFound:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        # Handling general exceptions

        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Endpoint: GET /api/students/:id/"""

        try:
            # Retrieving the record using get_object() method annd serializing it using get_serializer() method. Here, the get_object() method returns a single object from the queryset based on the primary key (pk) passed as parameter.

            student = self.get_object()
            student_serializer = self.get_serializer(student)

            # Returning the serialized data along with status code 200

            return Response(student_serializer.data, status=status.HTTP_200_OK)

        # Handling exceptions

        # Handling exception if the record is not found

        except exceptions.NotFound:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        # Handling general exceptions

        except Exception as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        """Endpoint: PUT /api/students/:id/"""

        try:
            # Retrieving the object/document which is to be updated using get_object() method.

            student = self.get_object()

            # serializing the student object using get_serializer() method & Fetching the data from the request, i.e. user has posted and de-serializing it using get_serializer() method.

            student_serializer = self.get_serializer(
                student, request.data, partial=True
            )

            # Checking the data if it is valid/de-serialized according to schema of the serializer_class

            if student_serializer.is_valid():

                # Saving the data into the serialized object, that has to be updated
                student_serializer.save()

                # Returning the updated data along with status code 200
                return Response(student_serializer.data, status=status.HTTP_200_OK)

            # Returning the errors if the data is not valid
            return Response(student_serializer.errors, status=status.HTTP_404_NOT_FOUND)

        # Handling exceptions

        # Handling exception if the record is not found

        except exceptions.NotFound:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        # Handling general exceptions

        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """Endpoint: DELETE /api/students/:id/"""

        try:
            # Retrieving the object/document which is to be deleted/destroyed using get_object() method & destroyning the object.

            student = self.get_object()
            self.perform_destroy(student)

            # Returning the status code 204 telling that the object is deleted
            return Response(status=status.HTTP_204_NO_CONTENT)

        # Handling exceptions

        # Handling exception if the record is not found

        except exceptions.NotFound:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        # Handling general exceptions

        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
