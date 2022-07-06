from django import forms


class SquareRootsForm(forms.Form):
    first = forms.IntegerField(label='first')
    second = forms.IntegerField(label='second')
    free = forms.IntegerField(label='free')
    imaginary_roots = forms.BooleanField(label='imaginary_roots',
                                         required=False)


class ItemsForm(forms.Form):
    selected_item = forms.IntegerField(label='selected_item')
    reveal = forms.BooleanField(label='reveal',
                                required=False)
