from django import forms
from .models import Poll

class PollForm(forms.Form):
    chosen_locations_options = forms.MultipleChoiceField(choices=[], label='Location Name', required=False,
                                                     widget=forms.SelectMultiple(
                                                        attrs={
                                                             'class': 'form-control'
                                                         }
                                                     ))
    other_location_name = forms.CharField(label='Other', max_length=100, required=False,
                                      widget=forms.TextInput(
                                        attrs={
                                              'class': 'form-control',
                                              'placeholder': 'Did we miss something?'
                                          }
                                      ))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        unique_locations_names = Poll.objects.order_by('location_name').values_list('location_name', flat=True).distinct()
        self.fields['chosen_locations_options'].choices = [(location_name, location_name) for location_name in unique_locations_names]