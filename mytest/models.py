from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
    	return u'%s' % (self.title)

class Version_question(models.Model):
    title = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    def __str__(self):
    	return u'%s' % (self.title)
    
