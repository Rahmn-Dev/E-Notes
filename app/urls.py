from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import api
from . import views

router = routers.DefaultRouter()
router.register("notes", api.notesApiViewSet)

urlpatterns = [
    path("", views.note_list, name="note list"),
    path("api/v2/", include(router.urls)),
    path("edit/<int:pk>/", views.note_edit, name="edit"),
    path("workspace/", views.workspace_create, name="workspacecreate"),
    path('admin/', admin.site.urls),
]
