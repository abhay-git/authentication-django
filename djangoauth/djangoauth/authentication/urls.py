from rest_framework import routers
from django.conf.urls import url , include , patterns
from authentication.views import AccountViewSet

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
]