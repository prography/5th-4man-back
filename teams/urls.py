from rest_framework import routers
from .views import TeamViewSet, TagViewSet

team_router = routers.SimpleRouter()
team_router.register(r'', TeamViewSet)
tag_router = routers.SimpleRouter()
tag_router.register(r'', TagViewSet)

urlpatterns = [
]
