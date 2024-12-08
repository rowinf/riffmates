from django.urls import path
from productivity import views

urlpatterns = [
    path("", views.productivity, name="productivity"),
    path("feeling_reports/<int:feeling_report_id>", views.edit_feeling_report, name="edit_feeling_report")
]
