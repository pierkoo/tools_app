from django import forms
from .models import Tools


# tu deklaruje formularze
class issueForm (forms.Form):
    # d=Tools.objects.get(pk=1)

    # c = [
    #     (d.name, d.name), ('T6', 'T633'),     ('T8', 'T67'),      ('T10', 'T789'),

    # ]


    # Generate list of list for choicefield
    at = Tools.objects.all()
    c = []
    for t in at:
        temp = (t.name, t.name)
        c.append(temp)


    tool_name = forms.ChoiceField(choices=c, label='Tool name: ')
    issue_qty = forms.IntegerField(label='Issue quantity:')


class MyForm(forms.Form):
    original_field = forms.CharField(required=False)
    extra_field_count = forms.IntegerField(required=False,widget=forms.HiddenInput())
    validate = forms.IntegerField(required=False, widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        extra_fields = kwargs.pop('extra', 0)
        check_valid = kwargs.pop('validate',0)


        if check_valid == '1':
            req_stat=True



        super(MyForm, self).__init__(*args, **kwargs)
        self.fields['original_field'].required = check_valid
        self.fields['extra_field_count'].initial = extra_fields

        if extra_fields:
            for index in range(int(extra_fields)):
                # generate extra fields in the number specified via extra_fields
                self.fields['extra_field_{index}'.format(index=index)] = \
                    forms.CharField(required=check_valid)

