from django import forms
from .models import*

class AddCommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ['content']
    
    def __init__(self, *args, **kwargs):
        super(AddCommentForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget.attrs['class'] = 'form-control'