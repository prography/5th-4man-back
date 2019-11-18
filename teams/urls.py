from rest_framework import routers
from .views import TeamViewSet

router = routers.SimpleRouter()
router.register(r'', TeamViewSet)

urlpatterns = [
]
urlpatterns += router.urls
