from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseBadRequest, HttpResponseNotAllowed
from django.shortcuts import render, redirect, get_object_or_404
from django.template.response import TemplateResponse
from django.utils import http

from productivity.forms import FeelingReportForm, JournalNoteForm, JournalTodoForm
from productivity.models import FeelingReport, JournalTodo, JournalNote


# Create your views here.

def productivity(request):

    context = {
        "title": "Productivity",
        "report_form": FeelingReportForm(),
        "note_form": JournalNoteForm(),
        "todo_form": JournalTodoForm(),
        "feeling_reports": request.user.feelingreport_set.all(),
        "todos": request.user.journaltodo_set.all(),
        "notes": request.user.journalnote_set.all(),
    }
    return render(request, "cotton/productivity.html", context)

@login_required
def edit_feeling_report(request, feeling_report_id=0):
    if feeling_report_id == 0:
        feeling_report_editing = FeelingReport.objects.create(owner=request.user,journal_id=1)
    else:
        feeling_report_editing = get_object_or_404(FeelingReport, id=feeling_report_id)

    if request.method == 'POST':
        form = FeelingReportForm(request.POST)

        if form.is_valid():
            feeling_report_editing.feeling = form.cleaned_data["feeling"]
            feeling_report_editing.description = form.cleaned_data["description"]
            # request.user.userprofile.musician_profiles.add(feeling_report_editing)
            feeling_report_editing.save()
            return redirect("productivity")
    return HttpResponseNotAllowed("POST")

@login_required
def edit_journal_todo(request, journal_todo_id=0):
    if journal_todo_id == 0:
        journal_todo_editing = JournalTodo.objects.create(owner=request.user, priority=1, journal_id=1)
    else:
        journal_todo_editing = get_object_or_404(JournalTodo, id=journal_todo_id)
    if request.method == "POST":
        form = JournalTodoForm(request.POST)

        if form.is_valid():
            journal_todo_editing.content = form.cleaned_data["content"]
            journal_todo_editing.save()
            return redirect("productivity")
        else:
            return HttpResponseBadRequest(form.errors)
    return HttpResponseNotAllowed("POST")

@login_required
def edit_journal_note(request, journal_note_id=0):
    if journal_note_id == 0:
        journal_note_editing = JournalNote.objects.create(owner=request.user, journal_id=1)
    else:
        journal_note_editing = get_object_or_404(JournalTodo, id=journal_note_id)
    if request.method == "POST":
        form = JournalNoteForm(request.POST)

        if form.is_valid():
            journal_note_editing.content = form.cleaned_data["content"]
            journal_note_editing.save()
            return redirect("productivity")
        else:
            return HttpResponseBadRequest(form.errors)
    return HttpResponseNotAllowed("POST")
