# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import zhcnet.ploneconf.site


class ZhcnetPloneconfSiteLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=zhcnet.ploneconf.site)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'zhcnet.ploneconf.site:default')


ZHCNET_PLONECONF_SITE_FIXTURE = ZhcnetPloneconfSiteLayer()


ZHCNET_PLONECONF_SITE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(ZHCNET_PLONECONF_SITE_FIXTURE,),
    name='ZhcnetPloneconfSiteLayer:IntegrationTesting'
)


ZHCNET_PLONECONF_SITE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(ZHCNET_PLONECONF_SITE_FIXTURE,),
    name='ZhcnetPloneconfSiteLayer:FunctionalTesting'
)


ZHCNET_PLONECONF_SITE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        ZHCNET_PLONECONF_SITE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='ZhcnetPloneconfSiteLayer:AcceptanceTesting'
)
