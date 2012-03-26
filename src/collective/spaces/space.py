from five import grok
from zope import schema
from plone.dexterity.content import Container
from plone.app.dexterity.interfaces import isValidId
from plone.directives import form
from plone.namedfile.field import NamedImage
from Products.GenericSetup.interfaces import IDAVAware

from collective.spaces import _


class ISpace(form.Schema):
    """Virtual collaboration workspace that acts as a navigation root.
    """

    custom_logo = NamedImage(
        title=_(u"Custom Logo"),
        description=_(u"Upload a custom logo to use for your Space."),
        required=False,
    )

    custom_logo_scale = schema.Choice(
        title=_(u"Custom Logo Size"),
        description=_(u"Select a size for your custom logo. The logo will "
                      u"automatically be scaled accordingly."),
        required=True,
        default="preview",
        vocabulary=u"collective.spaces.scales_vocabulary",
    )


class Space(Container):
    grok.implements(IDAVAware)
