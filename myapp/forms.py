# forms.py
from django import forms
from .models import Option, Question

class QuestionnaireForm(forms.Form):
    user = forms.CharField(max_length=255, label='Your Name')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
        questions = Question.objects.all()
        options = Option.objects.all()
        
        for question in questions:
            field_name = 'question_{}'.format(question.id)
            choices = [(option.id, '{} ({})'.format(option.text, option.marks)) for option in options]
            self.fields[field_name] = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(), label=question.text)
