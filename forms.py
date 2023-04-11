from django import forms

class feedback(forms.Form):
    name=forms.CharField()
    contact=forms.IntegerField()
    feedmsg=forms.CharField(widget=forms.Textarea)
