from django.conf.urls import url
from views import HospedeList, HospedeList_All, HospedeList_Inactive, HospedeCreate, HospedeDetail, HospedeUpdate, hospedes_delete

urlpatterns = [
    url(r'^$', HospedeList.as_view(), name='list'),
    url(r'^todos/$', HospedeList_All.as_view(), name='list_all'),
    url(r'^desativados/$', HospedeList_Inactive.as_view(), name='list_des'),
    url(r'^criar/$', HospedeCreate.as_view(), name='create'),
    url(r'^detalhe/(?P<pk>[\w-]+)$', HospedeDetail.as_view(), name='detail'),
    url(r'^editar/(?P<pk>[\w-]+)$', HospedeUpdate.as_view(), name='update'),
    url(r'^remover/(?P<pk>[\w-]+)$', hospedes_delete, name='delete'),
]