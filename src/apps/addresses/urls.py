from rest_framework import routers as r

from . import views as v

router = r.DefaultRouter()

router.register("addresses", v.AddressViewSet)

urlpatterns = router.urls
