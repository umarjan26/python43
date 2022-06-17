
from django.urls import path

from webapp.views import index_view, create

urlpatterns = {
    path("", index_view),
    path("articles/add/", create)
}