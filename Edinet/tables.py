import django_tables2 as tables
from Edinet.models import Client

class ClientTable(tables.Table):
    class Meta:
        model = Client
        template_name = "django_tables2/bootstrap-responsive.html"
        fields = ("ID_Client","Raison_sociale","Commercial","Adresse1","Adresse2","Code_postale","Ville","Pays")

        class Meta:
            attrs = {"class": "mytable"}