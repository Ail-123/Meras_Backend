from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Course
from .serializers import CourseSerializer

@api_view(['GET'])
def list_courses(request):
    courses = Course.objects.filter(is_published=True)
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)