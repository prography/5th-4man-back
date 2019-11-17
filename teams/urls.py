from rest_framework import routers
from .views import TeamViewSet, TagViewSet

router = routers.SimpleRouter()
router.register(r'tags', TagViewSet)
router.register(r'', TeamViewSet)

urlpatterns = [
]

urlpatterns += router.urls
