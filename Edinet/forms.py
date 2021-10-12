from django import forms
from Edinet.models import Utilisateur, Client, Info_client

class  LoginForm(forms.Form):
	email = forms.EmailField(label='Courriel')
	password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)

	def clean(self):
		cleaned_data = super (LoginForm, self).clean()
		email = cleaned_data.get("email")
		password = cleaned_data.get("password")

		#Verifie que les 2 champs sont valides
		if email and password:
			result = Utilisateur.objects.filter(password=password, Email=email)
			if len(result) != 1:
				raise forms.ValidationError("Adresse mail ou mot de passe incorrect.")
		return cleaned_data

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = Utilisateur
		exclude = ('registration_number',)

class AddClientForm(forms.Form):
	raison_sociale = forms.CharField(label='Raison sociale:')
	
	def clean(self):
		cleaned_data = super (AddClientForm, self).clean()
		raison_sociale = cleaned_data.get("raison_sociale")
		return cleaned_data, raison_sociale	
