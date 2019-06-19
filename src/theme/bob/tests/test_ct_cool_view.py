# -*- coding: utf-8 -*-
from theme.bob.testing import THEME_BOB_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest


try:
    from plone.dexterity.schema import portalTypeToSchemaName
except ImportError:
    # Plone < 5
    from plone.dexterity.utils import portalTypeToSchemaName


class CoolViewIntegrationTest(unittest.TestCase):

    layer = THEME_BOB_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_ct_cool_view_schema(self):
        fti = queryUtility(IDexterityFTI, name='Cool View')
        schema = fti.lookupSchema()
        schema_name = portalTypeToSchemaName('Cool View')
        self.assertEqual(schema_name, schema.getName())

    def test_ct_cool_view_fti(self):
        fti = queryUtility(IDexterityFTI, name='Cool View')
        self.assertTrue(fti)

    def test_ct_cool_view_factory(self):
        fti = queryUtility(IDexterityFTI, name='Cool View')
        factory = fti.factory
        obj = createObject(factory)


    def test_ct_cool_view_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Cool View',
            id='cool_view',
        )


        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertIn('cool_view', self.parent.objectIds())

    def test_ct_cool_view_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Cool View')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_cool_view_filter_content_type_false(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Cool View')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'cool_view_id',
            title='Cool View container',
         )
        self.parent = self.portal[parent_id]
        obj = api.content.create(
            container=self.parent,
            type='Document',
            title='My Content',
        )
        self.assertTrue(
            obj,
            u'Cannot add {0} to {1} container!'.format(obj.id, fti.id)
        )
