 #-*- coding: utf-8 -*-
from django.db import models

#Utilisateurs de Edinet
class Utilisateur(models.Model):
	registration_number = models.CharField(max_length=10)
	Nom = models.CharField(max_length=30)
	Prenom = models.CharField(max_length=30)
	Date_de_naissance = models.DateField()
	Email = models.EmailField()
	Mobile = models.CharField(max_length=20)
	password = models.CharField(max_length=32)
		#affichae dans l'interface admin
	def __str__(self):
		return self.Prenom + ' ' + self.Nom

class Client(models.Model):
	ID_Client = models.CharField(max_length=10)
	Raison_sociale = models.CharField(max_length=255)
	Commercial = models.CharField(max_length=100)
	Adresse1 = models.CharField(max_length=255)
	Adresse2 = models.CharField(max_length=255)
	Code_postale = models.CharField(max_length=10)
	Ville = models.CharField(max_length=255)
	Pays= models.CharField(max_length=255)
	#affichae dans l'interface admin
	def __str__(self):
		return self.Raison_sociale

class Info_client(models.Model):
	ID_Client = models.ForeignKey('Client',on_delete=models.CASCADE)
	ID_Info = models.CharField(max_length=10)
	Reglement = models.CharField(max_length=255)
	Envoi_facture = models.DateField()
	Type_Client = models.CharField(max_length=255)
	Date_signature_contrat = models.DateField()
	def __str__(self):
		return self.ID_Info

class Contact(models.Model):
	ID_Client = models.ForeignKey('Client',on_delete=models.CASCADE)
	ID_Contact = models.CharField(max_length=10)
	Civilite = models.CharField(max_length=50)
	Prenom = models.CharField(max_length=255)
	Nom = models.CharField(max_length=255)
	Fixe = models.CharField(max_length=100)
	Mobile = models.CharField(max_length=100)
	Email = models.CharField(max_length=255)
	Adresse1 = models.CharField(max_length=255)
	Adresse2 = models.CharField(max_length=255)
	Code_postale = models.CharField(max_length=10)
	Ville = models.CharField(max_length=255)
	Pays = models.CharField(max_length=255)
	Contact_facturation = models.BooleanField()
	Fonction = models.CharField(max_length=255)
	def __str__(self):
		return self.Prenom + ' ' + self.Nom

class Prestation(models.Model):
	ID_Client = models.ForeignKey('Client',on_delete=models.CASCADE)
	ID_Prestation = models.CharField(max_length=10)
	Application = models.CharField(max_length=255)
	PPNB = models.IntegerField(null=True)
	APNB = models.IntegerField(null=True)
	PPCL = models.IntegerField(null=True)
	APCL = models.IntegerField(null=True)
	LIASSE = models.IntegerField(null=True)
	ARCHIV_AR = models.IntegerField(null=True)
	P_LRE = models.IntegerField(null=True)
	P_AVIS = models.IntegerField(null=True)