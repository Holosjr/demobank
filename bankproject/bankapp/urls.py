from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


app_name='bankapp'


urlpatterns = [

    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('inside/',views.inside,name='inside'),
    path('form/',views.form,name='form'),
path('rough/',views.rough,name='rough'),

# path('Update/',views.Update,name='Update'),
# path('Update/<int:id>/', views.Update, name='Updates'),
    path('branch/',views.MBranch,name='MBranch'),
    path('<slug:c_slug>/',views.MBranch,name='branch_by_dist'),


]
if settings.DEBUG:
     urlpatterns += static(settings.STATIC_URL,
                           document_root= settings.STATIC_ROOT)
     urlpatterns += static(settings.MEDIA_URL,
                           document_root= settings.MEDIA_ROOT)



# path('change/', views.PersonListView.as_view(), name='person_changelist'),
#     path('add/', views.PersonCreateView.as_view(), name='person_add'),
#     path('<int:pk>/', views.PersonUpdateView.as_view(), name='person_change'),
# path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),