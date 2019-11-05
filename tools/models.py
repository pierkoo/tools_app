from django.db import models

class Tools(models.Model): # tabela w bazie
	name=models.CharField(max_length=15)
	qty = models.PositiveIntegerField()

	def __str__(self):
		return '%s %s' % (self.name, self.qty) #string ,string i wartości

class Issues(models.Model): # tabela w bazie
	name=models.CharField(max_length=15)
	qty = models.PositiveIntegerField()
	created_on = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '%s %s' % (self.pk) #string ,string i wartości

	

# Create your models here.
