from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',                      views.index,                        name='index'),
    url(r'^api/update_position$',   views.api_update_position,          name='update_position'),
    url(r'^api/login$',             views.login,                        name='login'),
    url(r'^api/beacon/register$',   views.api_register_with_beacon,     name='register_with_beacon'),
    url(r'^api/beacon/unregister$', views.api_unregister_with_beacon,   name='unregister_with_beacon'),
]

