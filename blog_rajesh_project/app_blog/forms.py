from django import forms

class EmailSendForm(forms.Form):
    name=forms.CharField( label='NAME',)
    city =forms.CharField( label='CITY')
    form=forms.EmailField( label='FORM ')
    to = forms.EmailField( label='TO ')
    comments=forms.CharField(required=False,widget=forms.Textarea, label='COMMENT')

from app_blog.models import Comment
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['name','email','body']