# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from zhcnet.ploneconf.site.testing import ZHCNET_PLONECONF_SITE_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that zhcnet.ploneconf.site is properly installed."""

    layer = ZHCNET_PLONECONF_SITE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if zhcnet.ploneconf.site is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'zhcnet.ploneconf.site'))

    def test_browserlayer(self):
        """Test that IZhcnetPloneconfSiteLayer is registered."""
        from zhcnet.ploneconf.site.interfaces import (
            IZhcnetPloneconfSiteLayer)
        from plone.browserlayer import utils
        self.assertIn(IZhcnetPloneconfSiteLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = ZHCNET_PLONECONF_SITE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['zhcnet.ploneconf.site'])

    def test_product_uninstalled(self):
        """Test if zhcnet.ploneconf.site is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'zhcnet.ploneconf.site'))

    def test_browserlayer_removed(self):
        """Test that IZhcnetPloneconfSiteLayer is removed."""
        from zhcnet.ploneconf.site.interfaces import IZhcnetPloneconfSiteLayer
        from plone.browserlayer import utils
        self.assertNotIn(IZhcnetPloneconfSiteLayer, utils.registered_layers())
