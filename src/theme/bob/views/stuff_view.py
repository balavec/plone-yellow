# -*- coding: utf-8 -*-

from theme.bob import _
from Products.Five.browser import BrowserView

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class StuffView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('stuff_view.pt')

    def __call__(self):
        # Implement your own actions:
        self.msg = _(u'A stuff message')
        return self.index()
