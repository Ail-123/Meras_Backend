import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meras_backend.settings')

application = get_wsgi_application()

# --- الكود التالي سيبني قاعدة البيانات وحساب الإدارة تلقائياً ---
try:
    from django.core.management import call_command
    from django.contrib.auth import get_user_model
    
    # بناء الجداول
    call_command('migrate', interactive=False)
    
    # إنشاء حساب أدمن إذا لم يكن موجوداً
    User = get_user_model()
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@admin.com', 'admin1234')
except Exception:
    pass