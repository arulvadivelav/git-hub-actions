from django.urls import path
from .views import ProfileListCreateView, ProfileRetrieveUpdateView

urlpatterns = [
    path("profiles/", ProfileListCreateView.as_view(), name="profiles"),
    path("profiles/<int:pk>/", ProfileRetrieveUpdateView.as_view(), name="profile-detail"),
    # path("static-list/", StaticListAPIView.as_view(), name="static-list"),
    
]
