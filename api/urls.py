
from django.urls import path
from api.api_view.views import *
from .views import list_view,textDetail,createView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/',TestView.as_view()),
    path('',list_view,name="home"),
    path('detail/<str:slug>/',textDetail,name="detail"),
    path('create/',createView,name="create_view"),
]
