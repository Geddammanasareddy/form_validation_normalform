from django import forms
def check_for_a(value):
    if value[0]=='a':
        raise forms.ValidationError('starting with a')
def check_for_len(value):
    if len(value)>6:
        raise forms.ValidationError('lenght of the name')




class StudentForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[check_for_a,check_for_len])
    age=forms.IntegerField()
    email=forms.EmailField(validators=[check_for_len])