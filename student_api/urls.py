from django.urls import path, include

urlpatterns = [
    path("api/", include("student_api.urls")),

]
