from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Region,Game,Studio,Publisher,Console, Contributor,Gamerelease,Develops,Publishes
from .forms import ConsoleForm,ContributorForm,RegionForm,StudioForm,PublisherForm,GameForm, ReleaseDateForm
from django.core.exceptions import ObjectDoesNotExist
from django.db import connection
from datetime import date
from django import forms


def index(request):
    return HttpResponse("index")

def Consoleview(request):
    if request.method == 'POST':
        status = dict()
        form = ConsoleForm(request.POST)
        
        if form.is_valid():
            if form.cleaned_data['action'] == "none":
                status['error'] = "Invalid Action"
            elif form.cleaned_data['action'] == "insert":
                if Console.objects.filter(name = form.cleaned_data['consoleName']).exists():
                    status['error'] = "Record Exists in Database"
                else:
                    if int(form.cleaned_data['online']) != 3 and int(form.cleaned_data['discont']) != 3:
                        x = form.cleaned_data
                        Console(name = x['consoleName'], online = int(x['online']), numports = x['numports'], maker = x['maker'], discont = x['discont']).save()
                        status['success'] = "Added Record"
                    else:
                        status['error'] = "Invalid Data (online and/or discontinuted Field)"
            elif form.cleaned_data['action'] == "delete":
                if Console.objects.filter(name = form.cleaned_data['consoleName']).exists():
                    Console.objects.get(name = form.cleaned_data['consoleName']).delete()
                    status['success'] = "Record Deleted"
                else:
                    status['error'] = "Record Does Not Exist"
            else:
                if Console.objects.filter(name = form.cleaned_data['consoleName']).exists():
                    consoleDB = Console.objects.get(name = form.cleaned_data['consoleName'])
                    if form.cleaned_data['online'] != 3:
                        consoleDB.online = form.cleaned_data['online']
                    if form.cleaned_data['discont'] != 3:
                        consoleDB.discont = form.cleaned_data['discont']
                    if form.cleaned_data['maker'] != None:
                        consoleDB.maker = form.cleaned_data['maker']
                    if form.cleaned_data['numports'] != None:
                        consoleDB.numports = form.cleaned_data['numports']
                    consoleDB.save()   
                else:
                    status['success'] = "Record Does Not Exist"
            return render(request, 'console.html', { 'form': form, 'status':status } )
    else:
        form = ConsoleForm()

    return render(request, 'console.html', {'form': form})
def Contributorview(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContributorForm(request.POST)
        status = dict()
        if form.is_valid():
            if form.cleaned_data['action'] == "none":
                status['error'] = "Invalid Action"
            elif form.cleaned_data['action'] == "insert":
                #Check to see if the record exists
                if Contributor.objects.filter(firstname = form.cleaned_data['firstName'], lastname = form.cleaned_data['lastName']).exists():
                    status['error'] = "Contributor Exists in database"
                else:
                    contriDB = Contributor(firstname = form.cleaned_data['firstName'],  lastname = form.cleaned_data['lastName'])
                    contriDB.save()
                    status['success'] = "Contributor Added"
            elif form.cleaned_data['action'] == "delete":
                if Contributor.objects.filter(firstname = form.cleaned_data['firstName'], lastname = form.cleaned_data['lastName']).exists():
                    Contributor.objects.filter(firstname = form.cleaned_data['firstName'], lastname = form.cleaned_data['lastName']).delete()
                    status['success'] = "Removed Record"
                else:
                    status['error'] = "Contributor Does Not Exist"
            elif form.cleaned_data['action'] == "update":
                if Contributor.objects.filter(firstname = form.cleaned_data['firstName'], lastname = form.cleaned_data['lastName']).exists():
                    contriDB = Contributor.objects.get(firstname = form.cleaned_data['firstName'], lastname = form.cleaned_data['lastName'])
                    contriDB.firstname = form.cleaned_data['newFirstName']
                    contriDB.lastname = form.cleaned_data['newLastName']
                    contriDB.save()
                    status['success'] = "Updated Record"
                else:
                    status['error'] = "Could Not Find Record"
        return render(request, 'contributor.html', {'form': form, 'status': status})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContributorForm()

    return render(request, 'contributor.html', {'form': form})

def Regionview(request):
    if request.method == 'POST':
        status = dict()
        form = RegionForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['action'] == "none":
                status['error'] = "Invalid Action"
            elif form.cleaned_data['action'] == "insert":
                if Region.objects.filter(name = form.cleaned_data['regionName']).exists():
                    status['error'] = "Region Exist in Database"
                else:
                    Region(name = form.cleaned_data['regionName']).save()
                    status['success'] =  "Added Record"
            elif form.cleaned_data['action'] == "delete":
                if Region.objects.filter(name = form.cleaned_data['regionName']).exists():
                    Region.objects.get(name = form.cleaned_data['regionName']).delete()
                    status['success'] = "Deleted Record From database"
                else:
                    status['error']  = "Record does not exists"
            else:
                if Region.objects.filter(name = form.cleaned_data['regionName']).exists():
                    regionDb =  Region.objects.get(name = form.cleaned_data['regionName'])
                    regionDb.name = form.cleaned_data['newRegionName']
                    regionDb.save()
                    status['success'] = "Updated Record"
                else:
                    status['error'] = "Record Does Not Exist"
        return render(request, 'region.html', {'form': form, 'status': status})
    else:
        form = RegionForm()

    return render(request, 'region.html', {'form': form})

def Studioview(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        status = dict()
        form = StudioForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['action'] == "none":
                status['error'] = "Invalid Action"
            elif form.cleaned_data['action'] == "insert":
                if Studio.objects.filter(studioname = form.cleaned_data['studioName']).exists():
                    status['error'] = "Record Exists in Database"
                else:
                    Studio(studioname = form.cleaned_data['studioName'], location = form.cleaned_data['location'], founded = form.cleaned_data['founded']).save()
                    status['success'] = "Added Record"
            elif form.cleaned_data['action'] == "delete":
                if Studio.objects.filter(studioname = form.cleaned_data['studioName']).exists():
                    Studio.objects.get(studioname = form.cleaned_data['studioName']).delete()
                    status['success'] = "Deleted Record"
                else:
                    status['error'] = "Record Does Not Exist"
            else:
                if Studio.objects.filter(studioname = form.cleaned_data['studioName']).exists():
                    StudioDB = Studio.objects.get(studioname = form.cleaned_data['studioName'])
                    
                    if form.cleaned_data['location'] != "":
                        StudioDB.location = form.cleaned_data['location']

                    if form.cleaned_data['founded'] != None:
                        StudioDB.founded = form.cleaned_data['founded']

                    StudioDB.save()
                    status['success'] = "Record Updated"
                else:
                    status['error'] = "Record does not exist"
        return render(request, 'studio.html', {'form': form, 'status': status})
    else:
        form = StudioForm()
    return render(request, 'studio.html', {'form': form})

def Publisherview(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        status = dict()
        form = PublisherForm(request.POST)

        if form.is_valid():
            if form.cleaned_data['action'] == "none":
                status['error'] = "Invalid Action"
            elif form.cleaned_data['action'] == "insert":
                if Publisher.objects.filter(pubname = form.cleaned_data['pubName']).exists():
                    status['error'] = "Record Exists in Database"
                else:
                    Publisher(pubname = form.cleaned_data['pubName'], location = form.cleaned_data['location'], founded = form.cleaned_data['founded']).save()
                    status['success'] = "Added Record"
            elif form.cleaned_data['action'] == "delete":
                if Publisher.objects.filter(pubname = form.cleaned_data['pubName']).exists():
                    Publisher.objects.get(pubname = form.cleaned_data['pubName']).delete()
                    status['success'] = "Deleted Record"
                else:
                    status['error'] = "Record Does Not Exist"
            else:
                if Publisher.objects.filter(pubname = form.cleaned_data['pubName']).exists():
                    publishDB = Publisher.objects.get(pubname = form.cleaned_data['pubName'])
                    
                    if form.cleaned_data['location'] != "":
                        publishDB.location = form.cleaned_data['location']

                    if form.cleaned_data['founded'] != None:
                        publishDB.founded = form.cleaned_data['founded']

                    publishDB.save()
                    status['success'] = "Record Updated"
                else:
                    status['error'] = "Record does not exist"
        return render(request, 'publisher.html', {'form': form, 'status': status})
    else:
        form = PublisherForm()
    return render(request, 'publisher.html', {'form': form})

# Generic Game
def Gameview(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        status = dict()
        if form.is_valid():
            if form.cleaned_data['action'] == "none":
                status['error'] = "Invalid Error"
            elif form.cleaned_data['action'] == "insert":
                if Game.objects.filter(title = form.cleaned_data['title']).exists():
                    status['error'] = "Record Exists in Database"
                else:
                    if int(form.cleaned_data['online']) != 3:
                        x = form.cleaned_data
                        Game(title = x['title'], online = x['online'], numplayers = x['numplayers'], maingenre = x['maingenre']).save()
                        status['success'] = "Added Record"
                    else:
                        status['error'] = "Invalid option on Online Field"
            elif form.cleaned_data['action'] == "delete":
                if Game.objects.filter(title = form.cleaned_data['title']).exists():
                    Game.objects.get(title = form.cleaned_data['title']).delete()
                    status['success'] = "Delete Record"
                else:
                    status['error'] = "Record Does Not Exist"
            else:
                if Game.objects.filter(title = form.cleaned_data['title']).exists():
                    GameDB = Game.objects.get(title = form.cleaned_data['title'])
                    if form.cleaned_data['maingenre'] != "":
                        GameDB.maingenre = form.cleaned_data['maingenre']

                    if int(form.cleaned_data['online']) != 3:
                        GameDB.online = form.cleaned_data['online']

                    if form.cleaned_data['numplayers'] != None:
                        GameDB.numplayers = form.cleaned_data['numplayers']
                    GameDB.save()
                    status['success'] = "Record Updated"
                else:
                    status['error'] = "Record does Not Exists"
            return render(request, 'game.html', {'form': form, 'status': status})
    else:
        form = GameForm()

    return render(request, 'game.html', {'form': form})




def insertFullGame(request):
    if request.method == "POST":
        form = GameForm(request.POST)
        form.fields['action'].widget = forms.HiddenInput()
        form.fields['action'].required = False
        status = dict()
        if form.is_valid():
            if int(form.cleaned_data['online']) == 3:
                status['error'] = "Online Field Value is not valid"
            else:
                gameDB = {
                    'title': form.cleaned_data['title'],
                    'maingenre': form.cleaned_data['maingenre'],
                    'online': form.cleaned_data['online'],
                    'numplayers': form.cleaned_data['numplayers'],
                }
                request.session['insert'] = True
                request.session['gameObj'] = gameDB
                status['success'] = "Added Game Record"
                print("request.session: ", request.session['gameObj'])
                return HttpResponseRedirect("SelectPublish")
            return render(request, 'game.html', {'form': form, 'status':status})

    else:
        form = GameForm()

        request.session.flush()

        form.fields['action'].widget = forms.HiddenInput()
        form.fields['action'].required = False
        form.fields['title'].required = True
        form.fields['maingenre'].required = True
        form.fields['online'].required = True
        form.fields['numplayers'].required = True

    return render(request, 'game.html', {'form': form})





def SelectPublisher(request):
  # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PublisherForm(request.POST)
        status = dict()
        if request.session['insert']:
            form.fields['action'].widget = forms.HiddenInput()
            form.fields['action'].required = False
        if form.is_valid():
            if Publisher.objects.filter(pubname = form.cleaned_data['pubName']).exists():
                print("publisher exists")
                request.session['pub_id']= Publisher.objects.get(pubname = form.cleaned_data['pubName']).pubid
                status['success'] = "Found Record In Database"
                print("publisher requestion.session ", request.session['pub_id'])
                return HttpResponseRedirect("SelectStudio")
            else:
                status['error'] = "Could Not Find a Record in Database"
                status['link'] = "insertPublisher"
                return render(request, 'publisher.html', {'form': form, 'status': status})
    else:
        form = PublisherForm()
        if request.session['insert']:
            form.fields['action'].widget = forms.HiddenInput()
            form.fields['action'].required = False
    return render(request, 'publisher.html', {'form': form})


def insertPublisher(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PublisherForm(request.POST)
        status = dict()
        if request.session['insert']:
            form.fields['action'].widget = forms.HiddenInput()
            form.fields['action'].required = False
        if form.is_valid():
            pubDB = {
                'pubName': form.cleaned_data['pubName'],
                'location': form.cleaned_data['location'],
                'founded': form.cleaned_data['founded']
            }
            request.session['pubDB'] = pubDB
            status['success'] = "Added Record"
            print("Insertpublisher requestion.session ", request.session['pubDB'])

            return HttpResponseRedirect("SelectStudio")
    else:
        form = PublisherForm()
        if request.session['insert']:
            form.fields['action'].widget = forms.HiddenInput()
            form.fields['pubName'].required = False
            form.fields['location'].required = True
            form.fields['founded'].required = True
    return render(request, 'publisher.html', {'form': form})

def SelectStudio(request):
  # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = StudioForm(request.POST)
        status = dict()
        if request.session['insert']:
            form.fields['action'].widget = forms.HiddenInput()
            form.fields['action'].required = False
        if form.is_valid():
            if Studio.objects.filter(studioname = form.cleaned_data['studioName']).exists():
                request.session['studio_id']= Studio.objects.get(studioname = form.cleaned_data['studioName']).studioid
                status['success'] = "Found Record In Database"
                print("studio requestion.session ", request.session['studio_id'])

                return HttpResponseRedirect("SelectConsole")
            else:
                status['error'] = "Could Not Find a Record in Database"
                status['link'] = "SelectConsole"
                return render(request, 'studio.html', {'form': form, 'status': status})
    else:
        form = StudioForm()
        if request.session['insert']:
            form.fields['action'].widget = forms.HiddenInput()
            form.fields['action'].required = False
    return render(request, 'studio.html', {'form': form})

def insertStudio(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = StudioForm(request.POST)
        status = dict()
        if request.session['insert']:
            form.fields['action'].widget = forms.HiddenInput()
            form.fields['action'].required = False
        if form.is_valid():
            studioDB = {
                'studioName': form.cleaned_data['studioName'],
                'location': form.cleaned_data['location'],
                'founded': form.cleaned_data['founded']                
            }
            request.session['studioDB'] = studioDB
            status['success'] = "Added Record"             
            print("insertStudio requestion.session ", request.session['studioDB'])

            return HttpResponseRedirect("SelectConsole")
    else:
        form = StudioForm()
        if request.session['insert']:
            form.fields['action'].widget = forms.HiddenInput()
            form.fields['studioName'].required = False
            form.fields['location'].required = True
            form.fields['founded'].required = True
    return render(request, 'publisher.html', {'form': form})


def SelectConsole(request):
  # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ConsoleForm(request.POST)
        status = dict()
        if request.session['insert']:
            form.fields['action'].widget = forms.HiddenInput()
            form.fields['action'].required = False
        if form.is_valid():
            if Console.objects.filter(name = form.cleaned_data['consoleName']).exists():
                request.session['console_id'] = Console.objects.get(name = form.cleaned_data['consoleName']).consoleid
                status['success'] = "Found Record In Database"
                print("console requestion.session ", request.session['console_id'])
                return HttpResponseRedirect("SelectRegion")
            else:
                status['error'] = "Could Not Find a Record in Database"
                status['link'] = "SelectConsole"
                return render(request, 'console.html', {'form': form, 'status': status})
    else:
        form = ConsoleForm()
        if request.session['insert']:
            form.fields['action'].widget = forms.HiddenInput()
            form.fields['action'].required = False
            form.fields['consoleName'].required = True
    return render(request, 'console.html', {'form': form})

def insertConsole(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ConsoleForm(request.POST)
        status = dict()
        if request.session['insert']:
            form.fields['action'].widget = forms.HiddenInput()
            form.fields['action'].required = False
        if form.is_valid():
            if int(form.cleaned_data['online']) != 3 and int(form.cleaned_data['discont']) != 3:
                consoleDB = {
                    'consoleName': form.cleaned_data['consoleName'],
                    'online': int(form.cleaned_data['online']),
                    'discont': int(form.cleaned_data['discont']),                
                    'numports': form.cleaned_data['numports'],
                    'maker': form.cleaned_data['maker']
                }
            request.session['consoleDB'] = consoleDB
            status['success'] = "Added Record"
            print("insertConsole requestion.session ", request.session['consoleDB'])

            return HttpResponseRedirect("SelectRegion")
    else:
        form = ConsoleForm()
        if request.session['insert']:
            form.fields['action'].widget = forms.HiddenInput()
            form.fields['consoleName'].required = False
            form.fields['online'].required = True
            form.fields['numports'].required = True
            form.fields['maker'].required = True
            form.fields['discont'].required = True
    return render(request, 'publisher.html', {'form': form})

def SelectRegion(request):
  # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegionForm(request.POST)
        status = dict()
        if request.session['insert']:
            form.fields['action'].widget = forms.HiddenInput()
            form.fields['action'].required = False
        if form.is_valid():
            if Region.objects.filter(name = form.cleaned_data['regionName']).exists():
                request.session['region_id'] = Region.objects.get(name = form.cleaned_data['regionName']).regionid
                status['success'] = "Found Record In Database"
                print("publisher request.session ", request.session['region_id'])

                return HttpResponseRedirect("insertReleaseDate")
            else:
                status['error'] = "Could Not Find a Record in Database"
                status['link'] = "SelectRegion"
                return render(request, 'region.html', {'form': form, 'status': status})
    else:
        form = RegionForm()
        if request.session['insert']:
            form.fields['action'].widget = forms.HiddenInput()
            form.fields['action'].required = False
    return render(request, 'region.html', {'form': form})

def insertRegion(request):
  # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegionForm(request.POST)
        status = dict()
        if request.session['insert']:
            form.fields['action'].widget = forms.HiddenInput()
            form.fields['action'].required = False
        if form.is_valid():
            regionDB = {
                'regionName': form.cleaned_data['regionName']
            }
            request.session['regionDB'] = regionDB
            status['sucess'] = "Inserted correctly to database"
            return HttpResponseRedirect("insertReleaseDate")
    else:
        form = RegionForm()
        if request.session['insert']:
            form.fields['action'].widget = forms.HiddenInput()
            form.fields['action'].required = False
    return render(request, 'region.html', {'form': form})

def insertReleaseDate(request):
      # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = ReleaseDateForm(request.POST)
        status = dict()

        if form.is_valid():
            date = form.cleaned_data['reldate']
            print("date: ", date)
            req = request.session

            ConsoleDB = None
            PubDB = None
            StudioDB = None
            RegionDB = None

            if 'console_id' in request.session:
                ConsoleDB = Console.objects.get(consoleid = request.session['console_id'])
            else:
                print("hello")
                req = request.session['consoleDB']
                ConsoleDB = Console(name = req['consoleName'], online = req['discont'], numports = req['numports'], maker = req['maker'])
            
            if 'pub_id' in request.session:
                PubDB = Publisher.objects.get(pubid = request.session['pub_id'])
            else:
                req = request.session['pubDB']
                PubDB = Publisher(pubname = req['pubName'], location = req['location'], founded = req['founded'])

            if 'studio_id' in request.session:
                StudioDB = Studio.objects.get(studioid = request.session['studio_id'])
            else:
                req = request.session['studioDB']
                StudioDB = Studio(studioname = req['studioName'], location = req['location'], founded = req['founded'])
            
            if 'region_id' in request.session:
                RegionDB = Region.objects.get(regionid = request.session['region_id'])
            else:
                req = request.session['regionDB']
                RegionDB = Region(name = req['regionName'])

            req = request.session['gameObj']
            print("ConsoleDB", ConsoleDB.name)

            try:
                GameDB = Game.objects.get(title = req['title'], maingenre = req['maingenre'], online = req['online'], numplayers = req['numplayers'])
                print("passed try")
            except ObjectDoesNotExist:
                print("obj does not exist")
                GameDB = Game(title = req['title'], maingenre = req['maingenre'], online = req['online'], numplayers = req['numplayers'])

            ReleaseDateQuery = Gamerelease.objects.filter(regionid = RegionDB, consoleid = ConsoleDB, gameid = GameDB, reldate = date)
            
            print
            if ReleaseDateQuery.exists():
                print("Record Exists")
                status['error'] = "Record Exists"
            else:
                RegionDB.save()
                ConsoleDB.save()
                GameDB.save()
                StudioDB.save()
                PubDB.save()
                Gamerelease(regionid = RegionDB, consoleid = ConsoleDB, gameid = GameDB, reldate = date).save()

                Publishes(gameid = GameDB, pubid = PubDB).save()
                Develops(gameid = GameDB, studioid = StudioDB).save()

                status['success'] = "Added Record"

                return HttpResponseRedirect("insertContributor")
    else:
        form = ReleaseDateForm()
    return render(request, 'region.html', {'form': form})

def insertContributor(request):
    return HttpResponse("insertContributor")




