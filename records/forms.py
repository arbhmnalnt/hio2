from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field

from.models import FinalRecord

class FinalRecordForm(forms.ModelForm):
    user        =   forms.CharField(label='اسم المستخدم', max_length=50, required=False, disabled=True)
    ayada       =   forms.CharField(label='اسم العيادة', max_length=50, required=False, disabled=True)
    name        =   forms.CharField(label='اسم المنتفع ثلاثى على الاقل', max_length=50, required=True)
    age         =   forms.IntegerField(label='السن', required=False)
    naId        =   forms.CharField(label='الرقم القومى كاملا - 14 رقم', max_length=14),
    hioId       =   forms.IntegerField(label='رقم الحاسب', required=False)
    phone       =   forms.CharField(label='رقم التليفون', max_length=11),
    illType     =   forms.CharField(label='نوع / انواع المرض', max_length=11),
    drugType    =   forms.CharField(label='نوع / انواع العلاج بالترتيب ', max_length=255),
    drugAmount  =   forms.CharField(label='كمية / كميات العلاج بالترتيب ', max_length=255),
    drugUnit    =   forms.CharField(label='الوحدة / الوحدات العلاج بالترتيب ', max_length=255)

    class Meta:
        model = FinalRecord
        fields = ['user','ayada','name', 'naId',  'hioId','age', 'illType', 'drugType', 'drugAmount', 'drugUnit']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('user'),
            Field('ayada'),
            Field('name'),
            Field('naId'),
            Field('hioId'),
            Field('age'),
            Field('illType'),
            Field('drugType'),
            Field('drugAmount'),
            Field('drugUnit'),
        )
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control text-center'