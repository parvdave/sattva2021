from django.db import models
from phone_field import PhoneField
from django.core import validators

# Create your models here.
class Event(models.Model):
    eventslug = models.CharField(max_length=200,blank=True)
    eventType = models.CharField(max_length=200,blank=True)
    eventName = models.CharField(max_length=200,blank=True)
    deptName = models.CharField(max_length=200,blank=True)
    desc = models.TextField(max_length=1000,blank=True)
    rules = models.TextField(max_length=100000000000000000000,blank=True)
    content = models.TextField(max_length=1000,blank=True)
    url = models.TextField(max_length=200,blank=True)
    youtube = models.TextField(max_length=1000,blank=True)
    def __str__(self):
        return self.eventName+f" ({self.deptName}) {self.eventslug}"

# Models for forms


class SoloSinging(models.Model):
    name = models.CharField(max_length=200,blank=True)
    age = models.IntegerField(validators=[validators.MinValueValidator,validators.MaxValueValidator(25)],null=True)
    email = models.EmailField(max_length=200,blank=True)
    idlink = models.URLField(max_length=200,blank=True)
    address = models.TextField(max_length=300,blank=True)
    country = models.CharField(max_length=200,blank=True)
    phoneNum = models.PositiveBigIntegerField(blank=True)
    whatsapp = models.PositiveBigIntegerField(blank=True)
    contacted = models.BooleanField(default=False,blank=True)
    

class GroupSinging(models.Model):
    name_of_group = models.CharField(max_length=200,blank=True)
    number_of_members = models.IntegerField(blank=True)
    name_of_head = models.CharField(max_length=200,blank=True)
    # age = models.IntegerField(null=True)
    email = models.EmailField(max_length=200,blank=True)
    address = models.TextField(max_length=300,blank=True)
    country = models.CharField(max_length=200,blank=True)
    phoneNum = models.CharField(blank=True,max_length=13)
    whatsapp = models.CharField(max_length=10,blank=True)
    contacted = models.BooleanField(default=False,blank=True)

class MonoAct(models.Model):
    name = models.CharField(max_length=200,blank=True)
    age = models.IntegerField(validators=[validators.MinValueValidator,validators.MaxValueValidator(25)],null=True)
    email = models.EmailField(max_length=200,blank=True)
    idlink = models.URLField(max_length=200,blank=True)
    address = models.TextField(max_length=300,blank=True)
    country = models.CharField(max_length=200,blank=True)
    phoneNum = models.PositiveBigIntegerField(blank=True)
    whatsapp = models.PositiveBigIntegerField(blank=True)
    contacted = models.BooleanField(default=False,blank=True)

class ClassicalDance(models.Model):
    name = models.CharField(max_length=200,blank=True)
    age = models.IntegerField(validators=[validators.MinValueValidator,validators.MaxValueValidator(25)],null=True)
    email = models.EmailField(max_length=200,blank=True)
    idlink = models.URLField(max_length=200,blank=True)
    style = models.CharField(max_length=200,blank=True)
    address = models.TextField(max_length=300,blank=True)
    country = models.CharField(max_length=200,blank=True)
    phoneNum = models.CharField(blank=True,max_length=10)
    whatsapp = models.CharField(max_length=10,blank=True)
    contacted = models.BooleanField(default=False,blank=True)

class BeatBoxing(models.Model):
    name = models.CharField(max_length=200,blank=True)
    age = models.IntegerField(validators=[validators.MinValueValidator,validators.MaxValueValidator(25)],null=True)
    email = models.EmailField(max_length=200,blank=True)
    idlink = models.URLField(max_length=200,blank=True)
    address = models.TextField(max_length=300,blank=True)
    country = models.CharField(max_length=200,blank=True)
    phoneNum = models.PositiveBigIntegerField(blank=True)
    whatsapp = models.PositiveBigIntegerField(blank=True)
    contacted = models.BooleanField(default=False,blank=True)

class RapBattle(models.Model):
    name = models.CharField(max_length=200,blank=True)
    age = models.IntegerField(validators=[validators.MinValueValidator,validators.MaxValueValidator(25)],null=True)
    email = models.EmailField(max_length=200,blank=True)
    idlink = models.URLField(max_length=200,blank=True)
    address = models.TextField(max_length=300,blank=True)
    country = models.CharField(max_length=200,blank=True)
    phoneNum = models.PositiveBigIntegerField(blank=True)
    whatsapp = models.PositiveBigIntegerField(blank=True)
    contacted = models.BooleanField(default=False,blank=True)

class WesternDance(models.Model):
    name = models.CharField(max_length=200,blank=True)
    age = models.IntegerField(validators=[validators.MinValueValidator,validators.MaxValueValidator(25)],null=True)
    email = models.EmailField(max_length=200,blank=True)
    address = models.TextField(max_length=300,blank=True)
    country = models.CharField(max_length=200,blank=True)
    idlink = models.URLField(max_length=200,blank=True)
    phoneNum = models.CharField(blank=True,max_length=10)
    whatsapp = models.CharField(max_length=10,blank=True)
    style = models.CharField(max_length=200,blank=True)
    contacted = models.BooleanField(default=False,blank=True)

class Poetry(models.Model):
    name = models.CharField(max_length=200,blank=True)
    age = models.IntegerField(validators=[validators.MinValueValidator,validators.MaxValueValidator(25)],null=True)
    email = models.EmailField(max_length=200,blank=True)
    idlink = models.URLField(max_length=200,blank=True)
    address = models.TextField(max_length=300,blank=True)
    country = models.CharField(max_length=200,blank=True)
    phoneNum = models.PositiveBigIntegerField(blank=True)
    whatsapp = models.PositiveBigIntegerField(blank=True)
    contacted = models.BooleanField(default=False,blank=True)

class ShortFilms(models.Model):
    nameoffilm = models.CharField(max_length=200,blank=True)
    genreoffilm = models.IntegerField(null=True)
    name = models.EmailField(max_length=200,blank=True)
    idlink = models.URLField(max_length=200,blank=True)
    email = models.EmailField(max_length=300,blank=True)
    address = models.TextField(max_length=300,blank=True)
    country = models.CharField(max_length=200,blank=True)
    phoneNum = models.CharField(blank=True,max_length=10)
    whatsapp = models.CharField(max_length=10,blank=True)
    contacted = models.BooleanField(default=False,blank=True)

class AdVision(models.Model):
    name1 = models.CharField(max_length=200,blank=True)
    phoneNum1 = models.CharField(blank=True,max_length=10)
    college1 = models.CharField(max_length=200,blank=True)
    email1 = models.EmailField(max_length=200,blank=True)
    name2 = models.CharField(max_length=200,blank=True)
    phoneNum2 = models.CharField(blank=True,max_length=10)
    college2 = models.CharField(max_length=200,blank=True)
    email2 = models.EmailField(max_length=200,blank=True)
    name3 = models.CharField(max_length=200,blank=True)
    phoneNum3 = models.CharField(blank=True,max_length=10)
    college3 = models.CharField(max_length=200,blank=True)
    email3 = models.EmailField(max_length=200,blank=True)

class Turnaround(models.Model):
    name = models.CharField(max_length=200,blank=True)
    phoneNum = models.CharField(blank=True,max_length=10)
    college = models.CharField(max_length=200,blank=True)
    email = models.EmailField(max_length=200,blank=True)

class Bidweiser(models.Model):
    name1 = models.CharField(max_length=200,blank=True)
    phoneNum1 = models.CharField(blank=True,max_length=10)
    college1 = models.CharField(max_length=200,blank=True)
    email1 = models.EmailField(max_length=200,blank=True)
    name2 = models.CharField(max_length=200,blank=True)
    phoneNum2 = models.CharField(blank=True,max_length=10)
    college2 = models.CharField(max_length=200,blank=True)
    email2 = models.EmailField(max_length=200,blank=True)

class TazhaKhabar(models.Model):
    dayChoice =( 
    ("1", "Day 1 - Topic 1"), 
    ("2", "Day 2 - Topic 2"),
    ) 
    name = models.CharField(max_length=200,blank=True)
    phoneNum = models.CharField(blank=True,max_length=10)
    college = models.CharField(max_length=200,blank=True)
    email = models.EmailField(max_length=200,blank=True)
    day = models.CharField(choices = dayChoice, max_length=200) 

class HouseOfBattle(models.Model):
    name1 = models.CharField(max_length=200,blank=True)
    phoneNum1 = models.CharField(blank=True,max_length=10)
    college1 = models.CharField(max_length=200,blank=True)
    email1 = models.EmailField(max_length=200,blank=True)
    name2 = models.CharField(max_length=200,blank=True)
    phoneNum2 = models.CharField(blank=True,max_length=10)
    college2 = models.CharField(max_length=200,blank=True)
    email2 = models.EmailField(max_length=200,blank=True)

class MarketGuru(models.Model):
    name = models.CharField(max_length=200,blank=True)
    phoneNum = models.CharField(blank=True,max_length=10)
    college = models.CharField(max_length=200,blank=True)
    email = models.EmailField(max_length=200,blank=True)

class DanceWorkshop(models.Model):
    name = models.CharField(max_length=200,blank=True)
    phoneNum = models.CharField(blank=True,max_length=10)
    college = models.CharField(max_length=200,blank=True)
    email = models.EmailField(max_length=200,blank=True)
    age = models.IntegerField(null=True)

class StandUpWorkshop(models.Model):
    name = models.CharField(max_length=200,blank=True)
    phoneNum = models.CharField(blank=True,max_length=10)
    college = models.CharField(max_length=200,blank=True)
    email = models.EmailField(max_length=200,blank=True)
    age = models.IntegerField(null=True)

class InfluentialTrendsWorkshop(models.Model):
    name = models.CharField(max_length=200,blank=True)
    phoneNum = models.CharField(blank=True,max_length=10)
    college = models.CharField(max_length=200,blank=True)
    email = models.EmailField(max_length=200,blank=True)
    age = models.IntegerField(null=True)

class FitnessWorkshop(models.Model):
    name = models.CharField(max_length=200,blank=True)
    phoneNum = models.CharField(blank=True,max_length=10)
    college = models.CharField(max_length=200,blank=True)
    email = models.EmailField(max_length=200,blank=True)
    age = models.IntegerField(null=True)

class ActingWorkshop(models.Model):
    name = models.CharField(max_length=200,blank=True)
    phoneNum = models.CharField(blank=True,max_length=10)
    college = models.CharField(max_length=200,blank=True)
    email = models.EmailField(max_length=200,blank=True)
    age = models.IntegerField(null=True)

class Fifa(models.Model):
    name = models.CharField(max_length=200,blank=True)
    phoneNum = models.CharField(blank=True,max_length=10)

class RocketLeague(models.Model):
    name1 = models.CharField(max_length=200,blank=True)
    phoneNum1 = models.CharField(blank=True,max_length=10)
    rank1 = models.CharField(max_length=200,blank=True)
    name2 = models.CharField(max_length=200,blank=True)
    phoneNum2 = models.CharField(blank=True,max_length=10)
    rank2 = models.CharField(max_length=200,blank=True)
    name3 = models.CharField(max_length=200,blank=True)
    phoneNum3 = models.CharField(blank=True,max_length=10)
    rank3 = models.CharField(max_length=200,blank=True)

class PUBG(models.Model):
    name1 = models.CharField(max_length=200,blank=True)
    phoneNum1 = models.CharField(blank=True,max_length=10)
    tier1 = models.CharField(max_length=200,blank=True)
    name2 = models.CharField(max_length=200,blank=True)
    phoneNum2 = models.CharField(blank=True,max_length=10)
    tier2 = models.CharField(max_length=200,blank=True)
    name3 = models.CharField(max_length=200,blank=True)
    phoneNum3 = models.CharField(blank=True,max_length=10)
    tier3 = models.CharField(max_length=200,blank=True)
    name4 = models.CharField(max_length=200,blank=True)
    phoneNum4 = models.CharField(blank=True,max_length=10)
    tier4 = models.CharField(max_length=200,blank=True)

class MrMsSattva(models.Model):
    genderChoices = (
        (1,'Male'),
        (2,'Female'),
        (3,'Other'),
    )
    name = models.CharField(max_length=200,blank=True)
    phoneNum = models.CharField(max_length=10,blank=True)
    college = models.CharField(max_length=200,blank=True)
    city = models.CharField(max_length=200,blank=True)
    gender = models.CharField(choices=genderChoices,max_length=200)
    talent = models.CharField(blank=True,max_length=200)

class PunIntended(models.Model):
    genderChoices = (
        (1,'Male'),
        (2,'Female'),
        (3,'Other'),
    )
    name = models.CharField(max_length=200,blank=True)
    phoneNum = models.CharField(max_length=10,blank=True)
    college = models.CharField(max_length=200,blank=True)
    city = models.CharField(max_length=200,blank=True)
    gender = models.CharField(choices=genderChoices,max_length=200)

class PopCulture(models.Model):
    genderChoices = (
        (1,'Male'),
        (2,'Female'),
        (3,'Other'),
    )
    name1 = models.CharField(max_length=200,blank=True)
    phoneNum1 = models.CharField(max_length=10,blank=True)
    college1 = models.CharField(max_length=200,blank=True)
    city1 = models.CharField(max_length=200,blank=True)
    gender1 = models.CharField(choices=genderChoices,max_length=200)
    name2 = models.CharField(max_length=200,blank=True)
    phoneNum2 = models.CharField(max_length=10,blank=True)
    college2 = models.CharField(max_length=200,blank=True)
    city2 = models.CharField(max_length=200,blank=True)
    gender2 = models.CharField(choices=genderChoices,max_length=200)


class PhotographyContest(models.Model):
    name = models.CharField(max_length=200,blank=True)
    phoneNum = models.CharField(blank=True,max_length=10)
    whatsapp = models.CharField(blank=True,max_length=10)
    email = models.EmailField(max_length=200,blank=True)
    photo = models.BooleanField(default=False,blank=True)
    video = models.BooleanField(default=False,blank=True)


class PhotographyWorkshops(models.Model):
    name = models.CharField(max_length=200,blank=True)
    phoneNum = models.CharField(blank=True,max_length=10)
    whatsapp = models.CharField(blank=True,max_length=10)
    email = models.EmailField(max_length=200,blank=True)
    basicsofphoto = models.BooleanField(default=False,null=True)
    lightpainting = models.BooleanField(default=False,null=True)
    portrait = models.BooleanField(default=False,null=True)
    # interest = models.CharField(choices=workshopChoices,max_length=200)


# LAFA

class GlamUp(models.Model):
    name = models.CharField(max_length=200,blank=True)
    phoneNum = models.CharField(blank=True,max_length=10)
    college = models.CharField(blank=True,max_length=200)
    age = models.IntegerField(validators=[validators.MinValueValidator(16),validators.MaxValueValidator(21)],null=True)
    city = models.CharField(blank=True,max_length=200)
    email = models.EmailField(max_length=200,blank=True)
    idlink = models.URLField(max_length=200,blank=True)
    youtube = models.URLField(max_length=200,blank=True)

class Charades(models.Model):
    playing  = (
        (1,'Solo'),
        (2,'In a pair'),
        (3,'In a group of 3'),
    )
    name = models.CharField(max_length=200,blank=True)
    phoneNum = models.CharField(blank=True,max_length=10)
    college = models.CharField(blank=True,max_length=200)
    age = models.IntegerField(validators=[validators.MinValueValidator(16),validators.MaxValueValidator(25)],null=True)
    city = models.CharField(blank=True,max_length=200)
    email = models.EmailField(max_length=200,blank=True)
    howplay = models.CharField(max_length=200,choices=playing)
    groupname = models.CharField(max_length=200,blank=True)
