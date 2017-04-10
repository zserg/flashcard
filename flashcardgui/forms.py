from django import forms


class CardForm(forms.Form):
    deck = forms.CharField(label='Deck', max_length=100)
    question = forms.CharField(label='Front', widget=forms.Textarea)
    answer = forms.CharField(label='Back', widget=forms.Textarea)
