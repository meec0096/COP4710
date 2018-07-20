from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Region,Game,Studio,Publisher,Console, Contributor
from .forms import insertGameForm, insertStudioForm, insertRegionConsoleForm,insertContributorForm
from django.core.exceptions import ObjectDoesNotExist
from django.db import connection
from datetime import date
def index(request):
    # Post Request
    if request.method == 'POST':
        form = insertGameForm(request.POST)
        if form.is_valid():
            # if the text field for numplayers is negative or zero 
            if form.cleaned_data['numplayers'] < 1:
                print("\tnumplayers is incorrect value")
                form = insertGameForm()
            else:
                # Check if it already exist in database
                try:
                    game = Game.objects.get(title = form.cleaned_data['title'])
                    ''' Print Message stating that game already exist ''' 
                    return HttpResponse("Game Exist in database")
                except ObjectDoesNotExist:                
                    title = form.cleaned_data['title']
                    maingenre = form.cleaned_data['maingenre'] 
                    online = form.cleaned_data['online'] 
                    numplayers = form.cleaned_data['numplayers']

                    # Create query to insert into database 
                    gameDB = """INSERT INTO Game(title, maingenre, online, numplayers) VALUES ("{0}", "{1}", {2}, {3}); """ .format( title, maingenre, int(online), numplayers)
                    # Store into SESSION
                    request.session['gameDB'] = gameDB
                   
                    return HttpResponseRedirect('StudioPublish')

    # if a GET (or any other method) we'll create a blank form
    else:
        request.session.flush()
        form = insertGameForm()

    return render(request, 'index.html', {'form': form})

def StudioPublish(request):
     # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = insertStudioForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # if studioFounded or pubFounded are negative make user reinput data
            if form.cleaned_data['studioFounded'] < 1 or form.cleaned_data['pubFounded'] < 1:
                form = insertStudioForm()
            else:
                try:
                    # Check if the studio is already in the database
                    studioDB = Studio.objects.get(studioname = form.cleaned_data['studioName'])
                    request.session['studio'] = studioDB.studioid
                except ObjectDoesNotExist:
                    #Studio does not exist, create it
                    studioName = form.cleaned_data['studioName']
                    studioLocation = form.cleaned_data['studioLocation']
                    studioFounded = form.cleaned_data['studioFounded']
                    studioDB = """INSERT INTO studio(StudioName, location, founded) VALUES ("{0}", "{1}", {2});""" .format(studioName, studioLocation,studioFounded)
                    request.session['studioDB'] = studioDB
                try:
                    # Check if the publisher is already in the database
                    publisherDB = Publisher.objects.get(pubname = form.cleaned_data['pubName'])
                    request.session['publisher'] = publisherDB.pubid
                except ObjectDoesNotExist:
                    #Publisher does not exist, create it 
                    pubName = form.cleaned_data['pubName']
                    pubLocation = form.cleaned_data['pubLocation']
                    pubFounded = form.cleaned_data['pubFounded']
                    pubDB = """INSERT INTO publisher(PubName, location, founded) VALUES ("{0}", "{1}", {2});""" .format(pubName, pubLocation, pubFounded)
                    request.session['pubDB'] = pubDB 
                    print("redirecting to region console")
                return HttpResponseRedirect("RegionConsole")
    else:
        form = insertStudioForm()

    return render(request, 'index.html', {'form': form})

def RegionConsole(request):
    if request.method == 'POST':
        form = insertRegionConsoleForm(request.POST)
        if form.is_valid():
            try:
                regionDB = Region.objects.get(name = form.cleaned_data['regionName'])
                request.session['region'] = regionDB.regionid
            except ObjectDoesNotExist:
                regionName = form.cleaned_data['regionName']
                request.session['regionDB'] = """INSERT INTO REGION(name) VALUES ("{0}");""" . format(regionName)

            try:
                consoleDB = Console.objects.get(name = form.cleaned_data['ConsoleName'])
                request.session['console'] = consoleDB.consoleid
            except:
                consoleName = form.cleaned_data['ConsoleName']
                online = form.cleaned_data['online']
                numports = form.cleaned_data['numports']
                maker = form.cleaned_data['maker']
                discont = form.cleaned_data['discont']

                consoleDB = """INSERT INTO Console(name, online, numports, maker, discont) VALUES ("{0}",{1},{2},"{3}",{4}); """  .format(consoleName, online, numports, maker, discont)

                request.session['consoleDB'] = consoleDB
            return HttpResponseRedirect('Contributor')
    else:
        form = insertRegionConsoleForm()

    return render(request, 'index.html', {'form': form})

def Contributorview(request):
    if request.method == 'POST':
        form = insertContributorForm(request.POST)            
        if form.is_valid():
            try:
                contributorDB = Contributor.objects.get(firstname = form.cleaned_data['firstName'], lastname = form.cleaned_data['lastName'])
                request.session['contributor'] = contributorDB.contrid
            except ObjectDoesNotExist:              
                contributorDB = """INSERT INTO contributor(FirstName, LastName) VALUES ("{0}", "{1}"); """ .format(form.cleaned_data['firstName'], form.cleaned_data['lastName'])
                request.session['contributorDB'] = contributorDB

            '''Have Finished collecting all of the data for inserting to database''' 
            with connection.cursor() as cursor:
                cursor.execute(request.session['gameDB'])

                # gets the primary key of the last inserted tuple
                gameID = cursor.lastrowid

                if 'studio' not in request.session:
                    cursor.execute(request.session['studioDB'])
                    request.session['studio'] = cursor.lastrowid

                cursor.execute("INSERT INTO Develops(studioid, gameid) VALUES ({0},{1});" .format(request.session['studio'], gameID))
                if 'publisher' not in request.session:
                    cursor.execute(request.session['pubDB'])
                    request.session['publisher'] = cursor.lastrowid

                cursor.execute("INSERT INTO Publishes(pubid, gameid) VALUES ({0},{1});" .format(request.session['publisher'], gameID))
                if 'region' not in request.session:
                    cursor.execute(request.session['regionDB'])
                    request.session['region'] = cursor.lastrowid

                if 'console' not in request.session:
                    cursor.execute(request.session['consoleDB'])
                    request.session['console'] = cursor.lastrowid

                if 'contributor' not in request.session:
                    cursor.execute(request.session['contributorDB'])
                    request.session['contributor'] = cursor.lastrowid
                
                cursor.execute("INSERT INTO Contributes(contrid, gameid) VALUES ({0},{1});" .format(request.session['contributor'], gameID))

                cursor.execute("INSERT INTO Gamerelease(reldate, gameid, consoleid, regionid) VALUES ('{0}', {1}, {2}, {3});" .format(date(2018, 1, 2), gameID, request.session['console'], request.session['region']))
            return HttpResponse("Added Game")
    else:
        form = insertContributorForm()

    return render(request, 'index.html', {'form': form})
