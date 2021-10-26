from django import forms
from Edinet.models import Utilisateur, Client, Info_client

#Formulaire de connexion a l'intranet 
class  LoginForm(forms.Form):
	#Creation des champs
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

#register
class UserProfileForm(forms.ModelForm):
	class Meta:
		model = Utilisateur
		exclude = ('registration_number','Mobile')

#ajouter un client
class AddClientForm(forms.ModelForm):
	class Meta:
		model = Client
		fields = '__all__'
