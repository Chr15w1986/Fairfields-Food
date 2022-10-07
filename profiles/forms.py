""" Forms file for profiles app """
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import UserProfile


class UserForm(forms.ModelForm):
    """ Form class to reorder the fields shown """
    class Meta:
        model = UserProfile
        fields = ('first_name',
                  'last_name',
                  'street_address1',
                  'street_address2',
                  'town_or_city',
                  'county',
                  'postcode',
                  'email',
                  'phone_number')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'update-profile'))
