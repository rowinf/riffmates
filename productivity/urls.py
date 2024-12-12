from django.urls import path
from productivity import views

urlpatterns = [
    path("", views.productivity, name="productivity"),
    path("feeling_reports/<int:feeling_report_id>", views.edit_feeling_report, name="edit_feeling_report"),
    path("journal_notes/<int:journal_note_id>", views.edit_journal_note, name="edit_journal_note"),
    path("journal_todos/<int:journal_todo_id>", views.edit_journal_todo, name="edit_journal_todo")
]
