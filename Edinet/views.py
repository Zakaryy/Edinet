# -*- coding: utf-8 -*-
from Edinet.models import Utilisateur, Client, Info_client
from django.shortcuts import render, redirect
from datetime import datetime 
from Edinet.forms import LoginForm, UserProfileForm, AddClientForm
import pandas as pd

from django.views.generic import ListView, CreateView


def welcome(request):
	logged_user = get_logged_user_from_request(request)
	if logged_user:
		return render(request, 'welcome.html', {'logged_user': logged_user})
	else:
		return redirect('/login')
	
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

def get_logged_user_from_request(request):
	if 'logged_user_id' in request.session:
		logged_user_id = request.session['logged_user_id']
		if len(Utilisateur.objects.filter(id=logged_user_id)) == 1:
			return Utilisateur.objects.get(id=logged_user_id)
		else:
			return None
	else:
		return None

def clients(request):
	df = pd.DataFrame(list(Client.objects.all().values()))
	allData=[]
	for i in range(df.shape[0]):
		temp=df.loc[i]
		allData.append(dict(temp))
	context = {'data': allData}
	data = Client.objects.all().values()
	return render(request, 'clients.html', context)