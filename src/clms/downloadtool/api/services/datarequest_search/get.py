# -*- coding: utf-8 -*-
"""
For HTTP GET operations we can use standard HTTP parameter passing (through the URL)

"""
from plone import api
from plone.restapi.services import Service

from zope.component import getUtility
from clms.downloadtool.utility import IDownloadToolUtility

from logging import getLogger

log = getLogger(__name__)

class datarequest_search(Service):
    def reply(self):
        status_list = ["Rejected", "Queued", "In_progress", "Finished_ok", "Finished_nok", "Cancelled"]

        log.info('DATAREQUEST_SEARCH')
        utility = getUtility(IDownloadToolUtility)
        status = self.request.get("Status")
        user_id = str(self.request.get("UserID"))


        self.request.response.setStatus(200)
        response_json = utility.datarequest_search(user_id, status)
        if "Error, UserID not defined" in response_json:
            self.request.response.setStatus(400)
        
        if "Error, status not recognized" in response_json:
            self.request.response.setStatus(400)

        return response_json
