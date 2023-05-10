from django.shortcuts import render, redirect
from django.forms import inlineformset_factory

from projects.forms import ProjectModelForm

from projects.models import Project

# Create your views here.
class RegMod():
   def __init__(self, model, form_class, list_display=None, formset_model=None, formset_fields=None):
      self.model = model
      self.list_display = list_display # should be set to a list of the fields to display
      self.form_class = form_class
      self.formset_model = formset_model
      self.formset_fields = formset_fields
      
registered_models = []
registered_models.append(
   RegMod(
      model=Project,
      form_class=ProjectModelForm,
      list_display={}
   )
)


slug_context = {}
base_models = []
for regmodel in registered_models:
   # insert at the end of the file to maintain order of registered_models
   base_models.insert(-1, regmodel.model.__name__)
   # add to slug_context
   slug_context[f"{regmodel.model.__name__}"] = regmodel.model
base_context = {"models": base_models}



def defaultView(request):
   template_name = 'heistadmin/dashboard.djhtml'
   context = base_context
   for regmodel in registered_models:
      # add model to context
      context[f"{regmodel.model.__name__}"] = regmodel.model
      # insert at the end of the file to maintain order of registered_models

   return render(request, template_name, context)


def listView(request, slug):
   template_name = 'heistadmin/list_base.djhtml'
   context = base_context
   for regmodel in registered_models:
      if regmodel.model.__name__ == slug:
         active_model = regmodel.model

   context["slug"] = active_model.__name__
   context["objects"] = active_model.objects.all()
   context["prev_action_message"] = None # later
   

   return render(request, template_name, context)


def createView(request, slug):
   template_name = 'heistadmin/create_base.djhtml'
   context = base_context
   for regmodel in registered_models:
      if regmodel.model.__name__ == slug:
         active_model = regmodel
   
   if active_model.formset_model:
      BaseFormset = inlineformset_factory(active_model.model, active_model.formset_model, fields=active_model.formset_fields, extra=2)
      formset = BaseFormset()
      context["formset"] = formset

   context["slug"] = active_model.model.__name__
   context["form"] = active_model.form_class()
   if request.method == "POST":
      form = active_model.form_class(request.POST, request.FILES)
      if form.is_valid():
         form.save()
         return redirect('heistadmin:list', slug=slug)
      else:
         context["form"] = form
      # check if there is an inline formset and save it
      if active_model.formset_model:
         formset = BaseFormset(request.POST, instance=active_model.model.objects.first())
         if formset.is_valid():
            formset.save()
      # return reverse('heistadmin:list', args=[slug])

   

   return render(request, template_name, context)


def updateView(request, slug, pk):
   template_name = 'heistadmin/update_base.djhtml'
   context = base_context
   for regmodel in registered_models:
      if regmodel.model.__name__ == slug:
         active_model = regmodel
   instance = active_model.model.objects.get(id=pk)

   # if there is a formset
   if active_model.formset_model:
      BaseFormset = inlineformset_factory(active_model.model, active_model.formset_model, fields=active_model.formset_fields, extra=1)
      formset = BaseFormset(instance=instance)
      context["formset"] = formset

   if request.method == "POST":
      form = active_model.form_class(request.POST, request.FILES, instance=instance)
      if form.is_valid():
         form.save()
      instance = active_model.model.objects.get(id=pk)

      # check if there is an inline formset and save it
      if active_model.formset_model:
         formset = BaseFormset(request.POST, request.FILES, instance=instance)
         if formset.is_valid():
            formset.save()

   context["slug"] = active_model.model.__name__
   context["object"] = instance
   context["form"] = active_model.form_class(instance=instance)
   

   return render(request, template_name, context)


def deleteView(request, slug, pk):
   for regmodel in registered_models:
      if regmodel.model.__name__ == slug:
         active_model = regmodel
   instance = active_model.model.objects.get(id=pk)
   instance.delete()
   return redirect('heistadmin:list', slug=slug)

