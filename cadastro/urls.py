from django.conf.urls import include,url
from . import views

urlpatterns = [
    url(r'',views.cadastro_novo_usuario)
]

#requeste > url > view > model > response
