from django.contrib import admin
from django.urls import path, include, handler404, handler500

from .views import home
from .views import mention

from accounts.views import login_view
from accounts.views import essais1
from accounts.views import essais
from accounts.views import register_view
from accounts.views import logout_view
from accounts.views import mon_compte

from mes_aliments.views import mes_aliments
from mes_aliments.views import recherche
from mes_aliments.views import aliment_det
from mes_aliments.views import remplacement
from mes_aliments.views import error

from jeux.views import jeux



handler404 = "plateforme.views.handler404"
handler500 = "plateforme.views.handler500"

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', home),
    path('mention', mention),
    
    path('accounts/login/', login_view),
    path('accounts/essais/', essais),
    path('accounts/essais1/', essais1),
    path('accounts/register_view/', register_view),    
    path('accounts/logout_view/', logout_view),
    path('accounts/mon_compte/', mon_compte),

    path('mes_aliments/mes_aliments/', mes_aliments),
    path('mes_aliments/recherche/', recherche),
    path('mes_aliments/recherche/aliment_det', aliment_det),
    path('mes_aliments/remplacement', remplacement),
    path('mes_aliments/error', error),


    path('jeux/jeux/', jeux),


    
]
