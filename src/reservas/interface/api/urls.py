from .router import router
from reservas.service.views import VIEWS


def build_urls(_router):
    for prefix, viewset in VIEWS:
        _router.register(prefix, viewset)
    return _router.urls


urlpatterns = build_urls(router)
