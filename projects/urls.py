from projects.views import GalleryView, ProjectCreateView, ProjectDeleteView, ProjectDetailView, ProjectListView, ProjectUpdateView, projectPhotoUpdateView
from django.urls import path


app_name = 'projects'

urlpatterns = [
    path('', ProjectListView.as_view(), name='projectspage'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
    path('create/', ProjectCreateView.as_view(), name='project-create'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('<int:pk>/update/', ProjectUpdateView.as_view(), name='project-update'),
    path('<int:pk>/update/photos/', projectPhotoUpdateView, name='project-photo-update'),
    path('<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),
]
