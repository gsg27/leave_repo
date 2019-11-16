from django import forms
from django.forms import ModelForm
from leave_app.models import leave_model
from datetime import datetime

class leave_form(ModelForm):
     class Meta:
         model = leave_model
         exclude =[
                    'employee',
                ]
         fields = ('dept_name','leave_type','date_from','date_to','reason')




     def is_valid(self):

            valid=super(leave_form,self).is_valid()
            
            if not valid:
                return valid
        
            
            date_from=self.cleaned_data['date_from']
            date_to=self.cleaned_data['date_to']
            leave_type=self.cleaned_data['leave_type']
        

            if date_from<datetime.now().date():
                self.errors['date_from']=['Invalid from date']
                return False

            if(date_to<date_from):
                self.errors['date_to']=["Invalid to date"]

                return False
            return True
