# در فایل urls.py اپلیکیشن
from django.urls import path
from . import views

app_name = 'accounts'  # فضای نام برای اپلیکیشن

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    # سایر مسیرها
]
