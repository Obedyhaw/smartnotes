from django.forms import BaseModelForm
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from .models import Notes
from django.http import Http404, HttpResponse
from django.views.generic import CreateView,UpdateView,DeleteView
from .forms import NotesForm
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator


# Create your views here.
@login_required(login_url='/login')
def list(request):
    user_notes = Notes.objects.filter(user=request.user)
    return render(request, 'notes/notes_list.html', {'user_notes': user_notes})

@login_required(login_url='/login')
def all_notes(request):
    all_notes = Notes.objects.all()
    paginator = Paginator(all_notes, 6)
    page_number = request.GET.get('page')
    notes = paginator.get_page(page_number)
    return render(request, 'notes/notes_all.html', {'notes':notes})



def detail(request,pk): 
    try:
        note= Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
       return render(request,'notes/notes_error.html')
    return render(request, 'notes/notes_detail.html', {'note':note})

class NotesCreateview(LoginRequiredMixin,CreateView):
    model=Notes
    success_url='/smart/notes'
    form_class = NotesForm
    login_url='firstapp/login'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user= self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# class NotesUpdateView(UpdateView):
#         model=Notes
#         success_url='/smart/notes'
#         form_class = NotesForm 

class NotesUpdateView(LoginRequiredMixin,UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm

    def dispatch(self, request, *args, **kwargs):
        # Get the current instance of the Notes model
        self.object = self.get_object()

        # Check if the current user is the author of the notes
        if self.object.user != request.user:
            raise Http404("You do not have permission to access this page.")

        return super().dispatch(request, *args, **kwargs)


class NotesDeleteView(DeleteView):
    model=Notes
    success_url='/smart/notes'
    template_name='notes/notes_delete.html'
