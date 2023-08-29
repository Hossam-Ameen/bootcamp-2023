from rest_framework.views import APIView
from .models import Student
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerializer
from django.shortcuts import get_object_or_404


class StudentAPIView(APIView):
    serializer_class = StudentSerializer
    query_set = Student.objects.all()

    def get_object(id):
        pass

    def get(self, request, id=None):
        if id:
            student = get_object_or_404(Student, id=id)
            student_serializer = self.serializer_class(student)
        else:

            student_serializer = self.serializer_class(self.query_set, many=True)
        return Response(student_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        student_serializer = self.serializer_class(data=request.data)
        student_serializer.is_valid(raise_exception=True)
        student_serializer.save()
        return Response(student_serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request, id):
        student = Student.objects.filter(id=id).first()
        if student is None:
            return Response({"details": "student is not found"},
                            status=status.HTTP_404_NOT_FOUND)
        student_serializer = self.serializer_class(student, data=request.data,
                                               partial=True)
        student_serializer.is_valid(raise_exception=True)
        student_serializer.save()
        return Response(student_serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        student = Student.objects.filter(id=id).first()
        if student is None:
            return Response({"details": "student is not found"},
                            status=status.HTTP_404_NOT_FOUND)
        student_serializer = self.serializer_class(student, data=request.data)
        student_serializer.is_valid(raise_exception=True)
        student_serializer.save()
        return Response(student_serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        student = Student.objects.filter(id=id).first()
        if student is None:
            return Response({"details": "student is not found"},
                            status=status.HTTP_404_NOT_FOUND)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
