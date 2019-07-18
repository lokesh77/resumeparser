from rest_framework.routers import DefaultRouter
from parser_app.api.views import ParserViewSet

router = DefaultRouter()
router.register(r'', ParserViewSet, basename='parsers')
urlpatterns = router.urls
