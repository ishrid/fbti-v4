from .models import Regolamenti , Classifiche, Categorie, Calendari

def regolamentiViews(request):
    return {'regolamenti': Regolamenti.objects.all(), }


def classificheViews(request):
    return {'classifiche': Classifiche.objects.all(), }
 


def categorieViews(request):
    return {'categorie': Categorie.objects.all(), }



def calendariViews(request):
    return {'calendari': Calendari.objects.all(), }    