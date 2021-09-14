from django import forms
from .models import Dashboard
#from django.core.exceptions import ValidationError

'''
    #Adding a custom validation method for Agreement
def clean(self):
  cleaned_data = self.cleaned_data
  io_value = self.cleaned_data.get('internal_only', True)
  ## Return value if True (checked)
  if io_value:
    return io_value
   ## Raise exception if not checked
  raise ValidationError('Must confirm that this link is working and dashboard has been shared to proceed')
'''
class DashboardForm(forms.ModelForm):

  class Meta:
    model = Dashboard
    #fields = '__all__'
    fields = ('dashboard_name', 'dashboard_description', 
              'dashboard_link','dashboard_owner', 'dashboard_source',
                'dashboars_business_unit','internal_only')

    #Change the labels in the form:
    labels = {
      'dashboard_name':'Name',
      'dashboard_description':'Description',
      'dashboard_link':'Link',
      'dashboard_owner':'Owner/Point of contact',
      #'dashboard_tag':'tags', #I'm using this column to create the HTML tag used in the Landing page.
      'dashboard_source':'Source',
      'dashboars_business_unit':'Business Unit',
      'internal_only':'I confirm that the link is working and the dashboard has been shared.'
    }

  #I'm changing the text of the dropdown control from '- - - ' to 'Select.."
  def __init__(self, *args, **kwargs):
    super(DashboardForm, self).__init__(*args, **kwargs)
    self.fields['dashboars_business_unit'].empty_label = "Select..."
    self.fields['dashboard_source'].empty_label = "Select..."
    #Avoid validation for descrip
    self.fields['dashboard_description'].required = False
    #Force the check for Document shared and working link
    self.fields['internal_only'].required = True

