# -*- coding: utf 8 -*-
from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField

class Post(models.Model):
	TIPOS = (
			('POR', 'Porções'),
			('PAS', 'Pastéis'),
			('HOT', 'Hot-Dog'),
			('REF', 'Refrigerante'),
			('CER', 'Cerveja'),
			('COC', 'Coqueteis'),
			('MARK', 'Patrocínio')
	)
	name = models.CharField(max_length=100)
	tipos = models.CharField(max_length=6, choices=TIPOS)
	imagem = CloudinaryField('imagem',null=True, blank=True)
	texto = models.TextField(max_length=400, null=False, blank=False)

	def publish(self):
		self.save()

	def __str__(self):
		return self.tipos
