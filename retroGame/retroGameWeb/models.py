# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Console(models.Model):
    consoleid = models.AutoField(db_column='ConsoleID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=20, blank=True, null=True)
    online = models.IntegerField(blank=True, null=True)
    numports = models.IntegerField(db_column='numPorts', blank=True, null=True)  # Field name made lowercase.
    maker = models.CharField(max_length=20, blank=True, null=True)
    discont = models.IntegerField(db_column='Discont', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'console'

    def __str__(self):
        return self.name


class Contributes(models.Model):
    gameid = models.ForeignKey('Game', models.DO_NOTHING, db_column='GameID', primary_key=True)  # Field name made lowercase.
    contrid = models.ForeignKey('Contributor', models.DO_NOTHING, db_column='ContrID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contributes'
        unique_together = (('gameid', 'contrid'),)


class Contributor(models.Model):
    contrid = models.AutoField(db_column='ContrID', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contributor'

    def __str__(self):
        return self.firstname + " " + self.lastname

class Develops(models.Model):
    studioid = models.ForeignKey('Studio', models.DO_NOTHING, db_column='StudioID')  # Field name made lowercase.
    gameid = models.ForeignKey('Game', models.DO_NOTHING, db_column='GameID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'develops'
        unique_together = (('gameid', 'studioid'),)

class Game(models.Model):
    gameid = models.AutoField(db_column='GameID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=30, blank=True, null=True)
    maingenre = models.CharField(db_column='MainGenre', max_length=15, blank=True, null=True)  # Field name made lowercase.
    online = models.IntegerField(blank=True, null=True)
    numplayers = models.IntegerField(db_column='NumPlayers', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'game'

    def __str__(self):
        return self.title
    
class Gamerelease(models.Model):
    releaseid = models.AutoField(db_column='ReleaseID', primary_key=True)  # Field name made lowercase.
    reldate = models.DateField(db_column='RelDate', blank=True, null=True)  # Field name made lowercase.
    gameid = models.ForeignKey(Game, models.DO_NOTHING, db_column='GameID', blank=True, null=True)  # Field name made lowercase.
    consoleid = models.ForeignKey(Console, models.DO_NOTHING, db_column='ConsoleID', blank=True, null=True)  # Field name made lowercase.
    regionid = models.ForeignKey('Region', models.DO_NOTHING, db_column='RegionID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gamerelease'

    def __str__(self):
        return  "proiejafojaoifjaoifjaoifja"


class Publisher(models.Model):
    pubid = models.AutoField(db_column='PubID', primary_key=True)  # Field name made lowercase.
    pubname = models.CharField(db_column='PubName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(max_length=15, blank=True, null=True)
    founded = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'publisher'

    def __str__(self):
        return self.pubname


class Publishes(models.Model):
    gameid = models.ForeignKey(Game, models.DO_NOTHING, db_column='GameID', primary_key=True)  # Field name made lowercase.
    pubid = models.ForeignKey(Publisher, models.DO_NOTHING, db_column='PubID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'publishes'
        unique_together = (('gameid', 'pubid'),)


class Region(models.Model):
    regionid = models.AutoField(db_column='RegionID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'region'

    def __str__(self):
        return self.name


class Studio(models.Model):
    studioid = models.AutoField(db_column='StudioID', primary_key=True)  # Field name made lowercase.
    studioname = models.CharField(db_column='StudioName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(max_length=15, blank=True, null=True)
    founded = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'studio'

    def __str__(self):
        return self.studioname