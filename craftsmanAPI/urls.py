from django.urls import path
from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()
router.register('craftsmen', views.CraftsmanViewSet, basename='craftsman')

craftsmen_router = routers.NestedDefaultRouter(router, 'craftsmen', lookup='craftsman')
craftsmen_router.register('projects', views.ProjectViewSet, basename='craftsman-projects')
craftsmen_router.register('reviews', views.ReviewViewSet, basename='craftsman-reviews')

urlpatterns = router.urls + craftsmen_router.urls 