from django.db import models
from django.utils import timezone

#this stuff sets up/structures the database (and it kinda validates the data) 
class Course(models.Model):
    callnumber = models.CharField(unique=False, max_length=4, default='')
    name = models.CharField(unique=True, max_length=50)
    instructor = models.CharField(max_length=50)
    description = models.CharField(max_length=200, default='')
    term = models.CharField(max_length=50)
    students = models.ManyToManyField('Student')
    date = models.DateField(default=timezone.now)
    
    class Meta(object):
        verbose_name_plural = 'Courses'
        ordering = ('-date', 'name')
        
    def __unicode__(self):
        return u'%s | %s' % (self.callnumber, self.name)
    
    def save(self, *args, **kwargs):
    # "self" is a lot like "this" in javascript
        self.name = self.name.upper()
        super(Course, self).save(*args, **kwargs)

class Student(models.Model):
    name = models.CharField(unique=False, max_length=50)
    pid = models.CharField(unique=True, max_length=12)
    grade = models.IntegerField(max_length=3, null=True)
    
    class Meta(object):
        ordering = ('pid', 'name')
                    
    def __unicode__(self):
        return u'%s %s' % (self.name, self.pid)