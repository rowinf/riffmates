from django import forms

from productivity.models import FeelingReport, FeelingChoice


class FeelingReportForm(forms.Form):
    description = forms.CharField(widget=forms.Textarea(attrs={
        "rows": "3",
        "cols": "50",
        "class": "textarea"
    }), required=False)
    feeling = forms.ChoiceField(required=True, choices=FeelingChoice.choices,widget=forms.RadioSelect(attrs={
        "class": "control"
    }), label=None)

    def __init__(self, *args, **kwargs):
        super(FeelingReportForm, self).__init__(*args, **kwargs)
        self.fields["feeling"].label = ""

class JournalNoteForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={
        "rows": "3",
        "cols": "50",
    }))

class JournalTodoForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={
        "rows": "3",
    }))
    done = forms.BooleanField(required=False)