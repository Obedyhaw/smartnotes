from django.urls import path
 
from . import views


urlpatterns = [ 
  path('notes',views.list,name="notes.list"),
  path('notes/all',views.all_notes,name="notes.all"),
  path('notes/<int:pk>',views.detail,name="note.ju"),
  path('notes/<int:pk>/edit',views.NotesUpdateView.as_view(),name="notes.update"),
  path('notes/new', views.NotesCreateview.as_view(), name="notes.new"),
  path('notes/<int:pk>/delete',views.NotesDeleteView.as_view(),name="notes.delete"),
 ]