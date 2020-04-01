from project.choice import * 

class CViewerForm(forms.Form):

    kelas = forms.ChoiceField(choices = KELAS_CHOICES, label="", initial='', widget=forms.Select(), required=True)