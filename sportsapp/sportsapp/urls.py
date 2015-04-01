from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sportsapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'roster.views.home', name='home'),
    url(r'^sports/(?P<pk>\d+)$', 'roster.views.home', name='sports'),
    url(r'^teams/(?P<pk>\d+)$', 'roster.views.teams', name='teams'),
    url(r'^roster/(?P<pk>\d+)$', 'roster.views.roster', name='roster'),
    url(r'^player/(?P<pk>\d+)$', 'roster.views.player', name='player'),
    url(r'^teams_all/$', 'roster.views.teams_all', name='teams_all'),
    url(r'^players_all/$', 'roster.views.players_all', name='players_all'),

)
