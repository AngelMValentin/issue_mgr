from django.urls import path, include
from django.contrib import admin
from accounts import views 


urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
]