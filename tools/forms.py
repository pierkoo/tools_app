from django import forms
from .models import Tools


# tu deklaruje formularze
class issueForm (forms.Form):
    # Generate list of list for choicefield
    at = Tools.objects.all()
    c=[[e.name, e.name] for e in Tools.objects.all()]

    tool_name = forms.ChoiceField(choices=c, label='Tool name: ')
    issue_qty = forms.IntegerField(label='Issue quantity:')


class MyForm(forms.Form):

    choices=[[e.name, e.name] for e in Tools.objects.all()]

    tool_0 = forms.ChoiceField(choices=choices, required=False, label='Tool:')

    tool_qty_0 = forms.IntegerField(label='Issue quantity:',required=False)

    extra_field_count = forms.IntegerField(required=False,widget=forms.HiddenInput())

    validate = forms.IntegerField(required=False, widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        #choices=[[e.name, e.name] for e in Tools.objects.all()]
        extra_fields = kwargs.pop('extra', 0)
        check_valid = kwargs.pop('validate',0)

        super(MyForm, self).__init__(*args, **kwargs)

        self.fields['tool_0'].required = check_valid
        self.fields['tool_qty_0'].required = check_valid
        self.fields['extra_field_count'].initial = extra_fields

        if extra_fields:
            for index in range(int(extra_fields)):
                # generate extra fields in the number specified via extra_fields

                self.fields['tool_{index}'.format(index=index+1)] = \
                    forms.ChoiceField(choices=self.choices, required=check_valid, label='Tool:')

                self.fields['tool_qty_{index}'.format(index=index+1)] = \
                    forms.IntegerField(required=check_valid,
                        label='Issue quantity')
