from django.conf.urls import include, url

from zds_schema.routers import DefaultRouter

from orc.avg.api.viewsets import InzageVerzoekViewSet
from orc.brp.api.viewsets import NatuurlijkPersoonViewSet
from orc.mor.api.viewsets import MeldingOpenbareRuimteViewSet

from .schema import schema_view
from .viewsets import VerblijfsObjectViewSet

router = DefaultRouter()

router.register('brp/natuurlijkepersonen', NatuurlijkPersoonViewSet)

router.register('rsgb/verblijfsobjecten', VerblijfsObjectViewSet)

router.register('mor', MeldingOpenbareRuimteViewSet)

router.register('avg/inzageverzoeken', InzageVerzoekViewSet)


# TODO: the EndpointEnumerator seems to choke on path and re_path

urlpatterns = [
    url(r'^v(?P<version>\d+)/', include([

        # API documentation
        url(r'^schema/openapi(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=None),
            name='schema-json'),
        url(r'^schema/$',
            schema_view.with_ui('redoc', cache_timeout=None),
            name='schema-redoc'),

        # actual API
        url(r'^', include(router.urls)),
    ])),
]
