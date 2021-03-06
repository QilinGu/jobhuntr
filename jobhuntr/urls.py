from django.conf.urls import include, url
from django.contrib import admin

from haystack.query import SearchQuerySet
from haystack.views import SearchView
from haystack.forms import SearchForm

from search.views import countries


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # #url(r'.*', 'search.views.search', name='search'),
    url(r'^countries/$', countries, name='countries'),
    url(r'.*', SearchView(
            searchqueryset=SearchQuerySet().order_by('-added_on'),
            form_class=SearchForm
        )
    ),
]
