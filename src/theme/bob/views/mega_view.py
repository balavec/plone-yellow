# -*- coding: utf-8 -*-

from theme.bob import _
from Products.Five.browser import BrowserView

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class MegaView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('mega_view.pt')

    def __call__(self):
        # Implement your own actions:
        self.msg = _(u'A mega message')
        return self.index()
