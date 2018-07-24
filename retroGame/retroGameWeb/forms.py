from django import forms

BOOLEAN = ((3, " "), (1, "True"), (0, "False"))
db_action = (("none", " "),("insert", "Add New Record"), ("update", "Update Existing Record"), ("delete", "Remove Record") )

class GameForm(forms.Form):
    action = forms.ChoiceField(label = "Action:", widget = forms.Select(attrs = {'onchange': "changeRequired(); "}), choices = db_action)
    title = forms.CharField(max_length=30, label = "Title:", required = False)
    maingenre = forms.CharField(max_length = 15, label = "Genre:", required = False)
    online = forms.ChoiceField(label = "Online Supported:", choices = BOOLEAN, required = False)
    numplayers = forms.IntegerField(label = "Number of players:", required = False)
    
class PublisherForm(forms.Form):
    action = forms.ChoiceField(label = "Action:", widget = forms.Select(attrs = {'onchange': "changeRequired(); "}), choices = db_action)
    pubName  = forms.CharField(max_length = 30, label = "Publisher:", required = False)
    location = forms.CharField(max_length = 15, label=" Publisher's Location:", required = False)
    founded = forms.IntegerField(label = "Publisher founded:", required = False)

class StudioForm(forms.Form):
    action = forms.ChoiceField(label = "Action:", widget = forms.Select(attrs = {'onchange': "changeRequired(); "}), choices = db_action)
    studioName  = forms.CharField(max_length = 30, label = "Studio:", required = False)
    location = forms.CharField(max_length = 15, label="Studio's Location:", required = False)
    founded = forms.IntegerField(label = "Studio founded:", required = False)

class RegionForm(forms.Form):
    action = forms.ChoiceField(label = "Action:", widget = forms.Select(attrs = {'onchange': "changeRequired(); "}),choices = db_action)
    regionName = forms.CharField(max_length = 20, label = "Region:", required = True)
    newRegionName = forms.CharField(max_length = 20, label = "Region: ", widget = forms.HiddenInput(), required = False)

class ConsoleForm(forms.Form):
    action = forms.ChoiceField(label = "Action:", widget = forms.Select(attrs = {'onchange': "changeRequired(); "}), choices = db_action)
    consoleName = forms.CharField(max_length = 20, label = "Console:", required = False)
    online = forms.ChoiceField(label = "Online:", choices = BOOLEAN, required = False)
    numports = forms.IntegerField(label = "Number of Ports:", required = False)
    maker = forms.CharField(max_length = 20, label =  "Maker:", required = False)
    discont = forms.ChoiceField(label = "Discontinued? ", choices = BOOLEAN, required = False)

class ReleaseDateForm(forms.Form):
    reldate = forms.DateField(label = "Release Date:", input_formats = ['%Y/%m/%d'], widget = forms.DateInput(format = r"%Y/%m/%d"), required = True)

class ContributorForm(forms.Form):
    action = forms.ChoiceField(label = "Action:", widget = forms.Select(attrs = {'onchange': "changeRequired(); "}),choices = db_action)
    firstName = forms.CharField(max_length = 20, label = "First Name", required = True)
    lastName = forms.CharField(max_length = 20, label = "Last Name", required = True)
    newFirstName = forms.CharField(max_length = 20, label = " New First Name", widget = forms.HiddenInput(), required = False)
    newLastName = forms.CharField(max_length = 20, label = " New Last Name", widget = forms.HiddenInput(), required = False)