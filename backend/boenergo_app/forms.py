from django import forms


class SquareRootsForm(forms.Form):
    first = forms.IntegerField(label='first')
    second = forms.IntegerField(label='second')
    free = forms.IntegerField(label='free')
    imaginary_roots = forms.BooleanField(label='imaginary_roots',
                                         required=False)
