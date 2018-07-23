from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Region,Game,Studio,Publisher,Console, Contributor
from .forms import ConsoleForm,ContributorForm,RegionForm,StudioForm,PublisherForm,GameForm
from django.core.exceptions import ObjectDoesNotExist
from django.db import connection
from datetime import date


def index(request):
    return HttpResponse("index")

def insertConsole(request):
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
def insertContributor(request):
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

def insertRegion(request):
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

def insertStudio(request):
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

def insertPublisher(request):
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
def insertGame(request):
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