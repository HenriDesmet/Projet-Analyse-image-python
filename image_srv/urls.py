# Django imports
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

# App imports
import pi_im.views as piim_views
from django.views.decorators.csrf import csrf_exempt
from pi_im import views

urlpatterns = [
    #New URLS
    path('form_sendfile/', piim_views.form_sendfile),
    path('image_research/', piim_views.image_research),
    path('image_research/<int:id>/', piim_views.image_research_result),
    path('listrefs/', piim_views.listreferences),
    path('reindex/', piim_views.reindex),
    #old URLS
path('Img_searchesList/', csrf_exempt(views.Img_searchesList.as_view())),
path('Img_searchesList/<int:id>/', csrf_exempt(views.Img_searchesList.as_view()))


]

urlpatterns = format_suffix_patterns(urlpatterns)