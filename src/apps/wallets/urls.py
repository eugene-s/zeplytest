from rest_framework import routers as r

from . import views as v

router = r.DefaultRouter()

router.register("wallets", v.WalletViewSet)

urlpatterns = router.urls
