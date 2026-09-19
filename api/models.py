from django.db import models

# جدول المجالات المهنية
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم المجال")
    
    def __str__(self):
        return self.name

# جدول الكورسات
class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name="اسم الكورس")
    trainer_name = models.CharField(max_length=100, verbose_name="اسم المدرب")
    price = models.CharField(max_length=50, verbose_name="السعر")
    description = models.TextField(verbose_name="الوصف")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses', verbose_name="المجال")
    
    def __str__(self):
        return self.title

# جدول الدروس (مرتبط بالكورس)
class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=200, verbose_name="عنوان الدرس")
    duration = models.CharField(max_length=20, verbose_name="مدة الدرس (مثل 15:00)")

    def __str__(self):
        return f"{self.title} - {self.course.title}"