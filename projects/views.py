from django.urls.base import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from projects.forms import PhotoFormset, PhotoModelForm, ProjectModelForm
from django.shortcuts import redirect, reverse, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Photo, Project

# Create your views here.
class ProjectListView(ListView):
    template_name = 'projects/project_list.html'
    queryset = Project.objects.all().order_by('-year')
    context_object_name = 'projects'


class GalleryView(ListView):
    template_name = 'projects/project_gallery.html'
    queryset = Project.objects.all()
    context_object_name = 'projects'


class ProjectDetailView(DetailView):
    template_name = 'projects/project_detail.html'
    queryset = Project.objects.all()
    context_object_name = 'project'


class ProjectCreateView(LoginRequiredMixin, CreateView):
    template_name = 'projects/project_create.html'
    form_class = ProjectModelForm

    def get_context_data(self, **kwargs):
        context = super(ProjectCreateView, self).get_context_data(**kwargs)
        context['photos_formset'] = PhotoFormset()
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        photo_formset = PhotoFormset(self.request.POST, self.request.FILES)
        if form.is_valid() and photo_formset.is_valid():
            return self.form_valid(form, photo_formset)
        else:
            return self.form_invalid(form, photo_formset)
    
    def form_valid(self, form, photo_formset):
        print('valid')
        self.object = form.save(commit=False)
        self.object.picture = self.request.FILES['picture']
        self.object.save()
        photos = photo_formset.save(commit=False)
        for photo in photos:
            photo.project = self.object
            photo.save()
        return redirect(reverse('projects:projectspage'))

    def form_invalid(self, form, photo_formset):
        print('invalid')
        if not photo_formset.is_valid():
            print('invalid formset')
        return self.render_to_response(
            self.get_context_data(form=form, photos_formset=photo_formset)
        )


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'projects/project_update.html'
    queryset = Project.objects.all()
    form_class = ProjectModelForm

    def get_context_data(self, **kwargs):
        context = super(ProjectUpdateView, self).get_context_data(**kwargs)
        context['pk'] = self.object.pk
        return context

    def get_success_url(self):
        return reverse('projects:projectspage')


def projectPhotoUpdateView(request, pk):
    project = Project.objects.get(id=pk)
    formset = PhotoFormset(instance=project)

    if request.method == 'POST':
        formset = PhotoFormset(request.POST, request.FILES, instance=project)
        if formset.is_valid():
            formset.save()
            return redirect(reverse_lazy("projects:project_detail", kwargs={'pk': pk}))

    template_name = 'projects/project_photos_update.html'
    context = {'formset': formset}
    return render(request, template_name, context)


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'projects/project_delete.html'
    queryset = Project.objects.all()
    form_class = ProjectModelForm

    def get_success_url(self):
        return reverse('projects:projectspage')