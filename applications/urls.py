from rest_framework import routers
from .views import ApplicationViewSet

router = routers.SimpleRouter()
router.register(r'', ApplicationViewSet)

urlpatterns = [
]

urlpatterns += router.urls
