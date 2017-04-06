from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.core, name='core'),
	url(r'^cerveja/$', views.cerveja, name='cerveja'),
	url(r'^porcoes/$', views.porcoes, name='porcoes'),
	url(r'^pasteis/$', views.pasteis, name='pasteis'),
	url(r'^hotdog/$', views.hotdog, name='hotdog'),
	url(r'^refrigerante/$', views.refrigerante, name='refrigerante'),
	url(r'^coqueteis/$', views.coqueteis, name='coqueteis'),
]