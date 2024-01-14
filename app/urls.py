from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import api
from . import views

router = routers.DefaultRouter()
router.register("notes", api.notesApiViewSet)

urlpatterns = [
    path("", views.index, name="index"),
    path("list/<int:pk>/", views.note_list, name="note_list"),
    path("api/v2/", include(router.urls)),
    path("edit/<int:pk>/", views.note_edit, name="edit"),
    path("trash/<int:pk>/", views.note_trash, name="trash"),
    path("trashlist/", views.note_trashlist, name="trashlist"),
    path("workspace/", views.workspace_create, name="workspacecreate"),
    path('admin/', admin.site.urls),
]
