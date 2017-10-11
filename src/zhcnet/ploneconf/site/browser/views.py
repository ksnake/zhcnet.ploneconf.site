from Products.Five.browser import BrowserView
from plone import api
from plone.dexterity.browser.view import DefaultView


class ContactView(BrowserView):
    """ Vue pour afficher un contact du type Zone de Secours
    """
    
    def services(self):
      results = []
      brains = api.content.find(context=self.context, portal_type='service')
      for brain in brains:
        service = brain.getObject()
        results.append({
          'title': brain.Title,
          'description': brain.Description,
          'url': brain.getURL(),
          'zone_de_secours': service.zone_de_secours,
          'responsable': service.responsable,
          'telephone': service.telephone,
          'mail': service.mail,
          'uuid': brain.UID,
          })
      return results

    def groupements(self):
      results = []
      brains = api.content.find(context=self.context, portal_type='groupement')
      for brain in brains:
        groupement = brain.getObject()
        results.append({
          'title': brain.Title,
          'description': brain.Description,
          'url': brain.getURL(),
          'zone_de_secours': groupement.zone_de_secours,
          'chef_de_groupement': groupement.chef_de_groupement,
          'siege': groupement.siege,
          'telephone': groupement.telephone,
          'mail': groupement.mail,
          'uuid': brain.UID,
          })
      return results

    def postes_de_secours(self):
      results = []
      brains = api.content.find(context=self.context, portal_type='poste_de_secours')
      for brain in brains:
        poste_de_secours = brain.getObject()
        results.append({
          'title': brain.Title,
          'description': brain.Description,
          'url': brain.getURL(),
          'zone_de_secours': poste_de_secours.zone_de_secours,
          'groupement': poste_de_secours.groupement,
          'officier_gestionnaire_de_poste': poste_de_secours.officier_gestionnaire_de_poste,
          'adresse': poste_de_secours.adresse,
          'telephone': poste_de_secours.telephone,
          'mail': poste_de_secours.mail,
          'uuid': brain.UID,
          })
      return results      

    def agents(self):
      results = []
      brains = api.content.find(context=self.context, portal_type='agent')
      for brain in brains:
        agent = brain.getObject()
        results.append({
          'title': brain.Title,
          'description': brain.Description,
          'url': brain.getURL(),
          'nom': agent.nom,
          'prenom': agent.prenom,
          'statut': agent.statut,
          'grade': agent.grade,
          'fonction': agent.fonction,
          'localisation': agent.localisation,
          'zone_de_secours': agent.zone_de_secours,
          'service': agent.service,
          'telephone': agent.telephone,
          'mail': agent.email,
          'uuid': brain.UID,
          })
      return results       

    def contacts(self):
      results = []
      brains = api.content.find(context=self.context, portal_type='contact')
      for brain in brains:
        contact = brain.getObject()
        results.append({
          'title': brain.Title,
          'description': brain.Description,
          'url': brain.getURL(),
          'telephone': contact.telephone,
          'mail': contact.mail,
          'localisation': contact.localisation,
          'uuid': brain.UID,
          })
      return results

      
      
class TestTabularContact(BrowserView):
    """ A test list of Contacts
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

		
		