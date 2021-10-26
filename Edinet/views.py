# -*- coding: utf-8 -*-
from datetime import datetime 
from django.shortcuts import render, redirect
from django.views.generic import ListView

from django_tables2 import SingleTableView

from Edinet.forms import LoginForm, UserProfileForm, AddClientForm
from Edinet.models import Utilisateur, Client, Info_client
from Edinet.tables import ClientTable

#Welcome page
def welcome(request):
	logged_user = get_logged_user_from_request(request)
	if logged_user:
		return render(request, 'welcome.html', {'logged_user': logged_user})
	else:
		return redirect('/login')

#login page
def login(request):
	#	#test si le formulaire est envoye
	if len(request.POST) > 0:
		form = LoginForm(request.POST)
		if form.is_valid():
			user_email = form.cleaned_data['email']
			logged_user = Utilisateur.objects.get(Email=user_email)
			request.session['logged_user_id'] = logged_user.id
			return redirect('/welcome')
		else:
			return render(request,'login.html', {'form': form})
	else:
		form = LoginForm()
	return render(request, 'login.html', {'form': form})

#Creer un compte
def register(request):
	if len(request.GET) > 0:
		form = UserProfileForm(request.GET)
		if form.is_valid():
			form.save()
			return redirect('/login')
		else:
			return render(request,'user_profile.html', {'form':form})
	else:
		form = UserProfileForm()
		return render(request,'user_profile.html', {'form':form})

#enregister les donnees de l'utilisateur authentifie
def get_logged_user_from_request(request):
	if 'logged_user_id' in request.session:
		logged_user_id = request.session['logged_user_id']
		if len(Utilisateur.objects.filter(id=logged_user_id)) == 1:
			return Utilisateur.objects.get(id=logged_user_id)
		else:
			return None
	else:
		return None

#afficher les clients
class ClientListView(SingleTableView):
	model = Client
	table_class = ClientTable
	template_name = 'clients.html'

#Ajouter un client a la base de donnee
def addClient(request):
	form = AddClientForm

	if request.method == 'POST':
		form = AddClientForm(request.POST)
		if form.is_valid():
			form.save()

	context = {'form':form}
	return render(request, 'add-client.html', context)
 
