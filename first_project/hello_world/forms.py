from django import forms
from django.core import validators

from hello_world.models import Topic, Webpage, AccessRecords, User, Task


#Using form validation we can add a check for empty fields
# Check for bots
# Adding a "Clean" method for the entire form


#Custom validation function
def check_name_begins_with_d(value):
    if value[0].lower() != 'd':
        raise forms.ValidationError("Needs to start with D")


class FormName(forms.Form):

    name = forms.CharField(validators=[check_name_begins_with_d])
    task = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField(required=False)
    verify_email = forms.EmailField(label='Enter your email again: ', required=False)
    start_date = forms.DateField(widget=forms.SelectDateWidget)

    bot_catcher = forms.CharField(required=False, widget=forms.HiddenInput,
                                  validators=[validators.MaxLengthValidator(0)])

    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError("GOTCHA BOT")
        return botcatcher

    #DJANGO HAS CORE BUILT IN VALIDATORS from django.core.validators
    def clean(self):
        all_clean_data = super().clean()

        email_clean = all_clean_data['email']
        vmail_clean = all_clean_data['verify_email']

        if email_clean != vmail_clean:
            raise forms.ValidationError("Email addresses do not match!")

# https://docs.djangoproject.com/en/3.0/topics/forms/modelforms/

class ModelFormTest(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['username','task','start_date']


class ModelFormUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']


