from django.conf.urls import url
from views import quartos_list, quartos_create, quartos_delete, quartos_update


# urlpatterns = [
#     url(r'^$', posts_list, name='list'),
#     url(r'^create/$', posts_create, name='create'),
#     url(r'^(?P<slug>[\w-]+)/$', posts_detail, name='detail'),
#     url(r'^(?P<slug>[\w-]+)/edit/$', posts_update, name='update'),
#     url(r'^delete/$', posts_delete, name='delete'),
# ]

urlpatterns = [
    url(r'^$', quartos_list, name='list'),
    url(r'^criar/$', quartos_create, name='create'),
    url(r'^(?P<numero>[\w-]+)/remover/$', quartos_delete, name='delete'),
    url(r'^(?P<numero>[\w-]+)/editar/$', quartos_update, name='update'),
]