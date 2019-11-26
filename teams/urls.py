from rest_framework import routers
from .views import TeamViewSet, TagViewSet, CommentViewSet

team_router = routers.SimpleRouter()
team_router.register(r'', TeamViewSet)
tag_router = routers.SimpleRouter()
tag_router.register(r'', TagViewSet)
comment_router = routers.SimpleRouter()
comment_router.register(r'', CommentViewSet)

urlpatterns = [
]
