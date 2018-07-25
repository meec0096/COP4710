from django import forms
from .models import Region,Game,Studio,Publisher,Console, Contributor,Gamerelease,Develops,Publishes
from django.core.exceptions import ObjectDoesNotExist
from django.db import connection
BOOLEAN = ((3, " "), (1, "True"), (0, "False"))
db_action = (("none", " "),("insert", "Add New Record"), ("update", "Update Existing Record"), ("delete", "Remove Record") )

class GameForm(forms.Form):
    action = forms.ChoiceField(label = "Action:", widget = forms.Select(attrs = {'onchange': "changeRequired(); "}), choices = db_action)
    title = forms.CharField(max_length=30, label = "Title:", required = False)
    maingenre = forms.CharField(max_length = 15, label = "Genre:", required = False)
    online = forms.ChoiceField(label = "Online Supported:", choices = BOOLEAN, required = False)
    numplayers = forms.IntegerField(label = "Number of players:", required = False)

    def HideAction(self):
        print("hello eric")
        self.fields['action'].widget = forms.HiddenInput()
        self.fields['action'].required = False

    def setRequired(self):
        self.fields['title'].required = True
        self.fields['maingenre'].required = True
        self.fields['online'].required = True
        self.fields['numplayers'].required = True

    def validate_data(self):
        if int(self.cleaned_data['online']) != 3:
            gameDB = {
                'title': self.cleaned_data['title'],
                'maingenre': self.cleaned_data['maingenre'],
                'online': self.cleaned_data['online'],             
                'numplayers': self.cleaned_data['numplayers'],
            }
            return gameDB
        return None

class PublisherForm(forms.Form):
    action = forms.ChoiceField(label = "Action:", widget = forms.Select(attrs = {'onchange': "changeRequired(); "}), choices = db_action)
    pubName  = forms.CharField(max_length = 30, label = "Publisher:", required = False)
    location = forms.CharField(max_length = 15, label=" Publisher's Location:", required = False)
    founded = forms.IntegerField(label = "Publisher founded:", required = False)
    
    def HideAction(self):
        self.fields['action'].widget = forms.HiddenInput()
        self.fields['action'].required = False

    def setSelect(self):
        self.fields['pubName'].required = True

    def setRequired(self):
        self.fields['pubName'].required = True
        self.fields['location'].required = True
        self.fields['founded'].required = True

    def validate_data(self):
        if self.cleaned_data['founded'] > 0:
            pubDB = {
                'pubName': self.cleaned_data['pubName'],
                'location': self.cleaned_data['location'],
                'founded': self.cleaned_data['founded']
            }
            return pubDB
        return None

class StudioForm(forms.Form):
    action = forms.ChoiceField(label = "Action:", widget = forms.Select(attrs = {'onchange': "changeRequired(); "}), choices = db_action)
    studioName  = forms.CharField(max_length = 30, label = "Studio:", required = False)
    location = forms.CharField(max_length = 15, label="Studio's Location:", required = False)
    founded = forms.IntegerField(label = "Studio founded:", required = False)

    def HideAction(self):
        self.fields['action'].widget = forms.HiddenInput()
        self.fields['action'].required = False

    def setSelect(self):
        self.fields['studioName'].required = True

    def setRequired(self):
        self.fields['studioName'].required = True
        self.fields['location'].required = True
        self.fields['founded'].required = True

    def validate_data(self):
        if self.cleaned_data['founded'] > 0:
            studioDB = {
                'pubName': self.cleaned_data['studioName'],
                'location': self.cleaned_data['location'],
                'founded': self.cleaned_data['founded']
            }
            return studioDB
        return None

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

    def HideAction(self):
        self.fields['action'].widget = forms.HiddenInput()
        self.fields['action'].required = False

    def setSelect(self):
        self.fields['consoleName'].required = True

    def setRequired(self):
        self.fields['consoleName'].required = True
        self.fields['online'].required = True
        self.fields['numports'].required = True
        self.fields['maker'].required = True
        self.fields['discont'].required = True

    def validate_data(self):
        if int(self.cleaned_data['online']) != 3 and int(self.cleaned_data['discont']) != 3:
            consoleDB = {
                'consoleName': self.cleaned_data['consoleName'],
                'online': int(self.cleaned_data['online']),
                'discont': int(self.cleaned_data['discont']),                
                'numports': self.cleaned_data['numports'],         
                'maker': self.cleaned_data['maker']
            }
            return consoleDB
        return None

class ReleaseDateForm(forms.Form):
    reldate = forms.DateField(label = "Release Date:", input_formats = ['%Y/%m/%d'], widget = forms.DateInput(format = r"%Y/%m/%d"), required = True)
    def HideAction(self):
        self.fields['action'].widget = forms.HiddenInput()
        self.fields['action'].required = False

    def setRequired(self):
        self.fields['reldate'].required = True

class ContributorForm(forms.Form):
    action = forms.ChoiceField(label = "Action:", widget = forms.Select(attrs = {'onchange': "changeRequired(); "}),choices = db_action)
    firstName = forms.CharField(max_length = 20, label = "First Name", required = True)
    lastName = forms.CharField(max_length = 20, label = "Last Name", required = True)
    newFirstName = forms.CharField(max_length = 20, label = " New First Name", widget = forms.HiddenInput(), required = False)
    newLastName = forms.CharField(max_length = 20, label = " New Last Name", widget = forms.HiddenInput(), required = False)

    def HideAction(self):
        self.fields['action'].widget = forms.HiddenInput()
        self.fields['action'].required = False

    def setRequired(self):
        self.fields['firstname'].required = True
        self.fields['lastname'].required = True

class SearchForm(forms.Form):
    console = forms.ModelChoiceField(queryset = Console.objects.all(), empty_label = "---", required = False)
    publisher = forms.ModelChoiceField(queryset = Publisher.objects.all(), empty_label = "---", required = False)
    studio = forms.ModelChoiceField(queryset = Studio.objects.all(), empty_label = "---", required = False)
    game = forms.ModelChoiceField(queryset = Game.objects.all(), empty_label = "---", required = False)
    region = forms.ModelChoiceField(queryset = Region.objects.all(), empty_label = "---", required = False)
    contributor = forms.ModelChoiceField(queryset = Contributor.objects.all(), empty_label = "---" , required = False)


    def validate_data(self):
        with connection.cursor() as cursor:
            cursor.execute("Select * from GameRelease, Studio, Publisher; ")
            rows = self.dictfetchall(cursor)
            if self.cleaned_data['game']:                
                rows = [item for item in rows if item['GameID'] == self.cleaned_data['game'].gameid]
            
            if self.cleaned_data['publisher']:
                rows = [item for item in rows if item['PubID'] == self.cleaned_data['publisher'].pubid]

            if self.cleaned_data['studio']:
                rows = [item for item in rows if item['StudioID'] == self.cleaned_data['studio'].studioid]

            if self.cleaned_data['console']:
                rows = [item for item in rows if item['ConsoleID'] == self.cleaned_data['console'].consoleid]

            if self.cleaned_data['region']:
                rows = [item for item in rows if item['RegionID'] == self.cleaned_data['region'].regionid]

            if self.cleaned_data['contributor']:
                rows = [item for item in rows if item['ContriID'] == self.cleaned_data['contributor'].contrid]

        return rows
        
    def dictfetchall(self,cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]