from django import forms

BOOLEAN = ((1, "True"), (0, "False"))
class insertGameForm(forms.Form):
    title = forms.CharField(max_length=30, label = "Title:")
    maingenre = forms.CharField(max_length = 15, label = "Genre:")
    online = forms.ChoiceField(label = "Online Supported:", choices = BOOLEAN)
    numplayers = forms.IntegerField(label = "Number of players:")

class insertStudioForm(forms.Form):
    studioName  = forms.CharField(max_length = 30, label = "Studio:")
    studioLocation = forms.CharField(max_length = 15, label="Studio's Location:")
    studioFounded = forms.IntegerField(label = "Studio founded: ")
    pubName  = forms.CharField(max_length = 30, label = "Publisher: ")
    pubLocation = forms.CharField(max_length = 15, label=" Publisher's Location:")
    pubFounded = forms.IntegerField(label = "Publisher founded:")

class insertRegionConsoleForm(forms.Form):
    regionName = forms.CharField(max_length = 20, label = "Region:")
    ConsoleName = forms.CharField(max_length = 20, label = "Console:")
    online = forms.ChoiceField(label = "Online:", choices = BOOLEAN)
    numports = forms.IntegerField(label = "Number of Ports:")
    maker = forms.CharField(max_length = 20, label =  "Maker:")
    discont = forms.ChoiceField(label = "Discontinued? ", choices = BOOLEAN)

class insertContributorForm(forms.Form):
    firstName = forms.CharField(max_length = 20, label = "First Name")
    lastName = forms.CharField(max_length = 20, label = "Last Name")