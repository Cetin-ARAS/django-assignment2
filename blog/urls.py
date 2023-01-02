from django.urls import path, include
from .views import student_api, student_api_get_update_delete

urlpatterns = [
    path("api/", include("student_api.urls")),
    path("student/", student_api),
    path("apstudenti/<int:pk>", student_api_get_update_delete),

]
