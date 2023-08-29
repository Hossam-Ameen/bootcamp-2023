
from rest_framework.decorators import api_view
from rest_framework.response import Response
from student.serializers import StudentSerializer
from rest_framework import status

from .models import Student


@api_view(["GET", "POST", "PUT", "PATCH", "DELETE"])
def student_api_view(request):

    if request.method == "GET":
        students = Student.objects.all().order_by('-id')
        student_serializer = StudentSerializer(students, many=True)
        return Response(student_serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        student_serializer = StudentSerializer(data=request.data)
        student_serializer.is_valid(raise_exception=True)
        student_serializer.save()
        return Response(student_serializer.data,
                        status=status.HTTP_201_CREATED)


@api_view(["PUT", "PATCH", "DELETE"])
def update_student(request, id):
    student = Student.objects.filter(id=id).first()
    if student is None:
        return Response({"details": "this student is not found"},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    partial = False
    if request.method == "PATCH":
        partial = True
    studnet_serializer = StudentSerializer(student, request.data, partial=partial)
    studnet_serializer.is_valid(raise_exception=True)
    studnet_serializer.save()
    return Response(studnet_serializer.data, status=status.HTTP_200_OK)



