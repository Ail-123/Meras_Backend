from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    trainer_name = serializers.CharField(source='trainer.username', read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'price', 'trainer_name', 'is_published']