from Products.Five.browser import BrowserView
from plone import api
from plone.dexterity.browser.view import DefaultView


class TabularContact(BrowserView):
    """ A list of Contacts
    """

    def contact(self):
        results = []
        brains = api.content.find(context=self.context, portal_type='contact')
        for brain in brains:
            talk = brain.getObject()
            results.append({
                'title': brain.Title,
                'description': brain.Description,
                'url': brain.getURL(),
                'telephone': ', '.join(contact.telephone),
                })
        return results