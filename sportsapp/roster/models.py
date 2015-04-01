from django.db import models

#this stuff sets up/structures the database (and it kinda validates the data) 
class Sport(models.Model):
    name = models.CharField(unique=True, max_length=50)
    description = models.CharField(max_length=700, default='')
    icon = models.CharField(max_length=70, default='')
    teams = models.ManyToManyField('Team')
    
    class Meta(object):
        verbose_name_plural = 'Sports'
        ordering = ('name',)
        
    def __unicode__(self):
        return u'%s' % self.name

class Team(models.Model):
    name = models.CharField(unique=True, max_length=50)
    coach = models.CharField(max_length=50)
    description = models.CharField(max_length=700, default='')
    players = models.ManyToManyField('Player')
    image = models.CharField(unique=False, max_length=200)
    
    class Meta(object):
        verbose_name_plural = 'Teams'
        ordering = ('name', 'coach')
        
    def __unicode__(self):
        return u'%s' % self.name

class Player(models.Model):
    first = models.CharField(unique=False, max_length=50)
    last = models.CharField(unique=False, max_length=12)
    year = models.CharField(max_length=25)
    city = models.CharField(unique=False, max_length=50)
    state = models.CharField(unique=False, max_length=50)
    animal = models.CharField(unique=False, max_length=50)
    image = models.CharField(unique=False, max_length=200)
    bio = models.CharField(max_length=700, default='')
    
    class Meta(object):
        ordering = ('last', 'first')
                    
    def __unicode__(self):
        return u'%s %s' % (self.first, self.last)
