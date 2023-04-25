from django import forms
def check_for_a(value):
    if value[0]=='a':
        raise forms.ValidationError('starting with a')
def check_for_len(value):
    if len(value)<6:
        raise forms.ValidationError('lenght of the name')




class StudentForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[check_for_a,check_for_len])
    age=forms.IntegerField()
    email=forms.EmailField()
    re_enter_email=forms.EmailField()
    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)


    def clean(self):
        e=self.cleaned_data['email']
        r=self.cleaned_data['re_enter_email']
        if e!=r:
            raise forms.ValidationError('not matched')
        
    def clean_data(self):
        bot=self.clean_data['botcatcher']
        if len(bot)>0:
            raise forms.ValidationError('bot')
        