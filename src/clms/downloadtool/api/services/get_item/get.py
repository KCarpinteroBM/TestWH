# -*- coding: utf-8 -*-
"""
For HTTP GET operations we can use standard HTTP parameter passing (through the URL)

"""
from plone import api
from plone.restapi.services import Service

from zope.component import getUtility
from clms.downloadtool.utility import IDownloadToolUtility
import json

# logger, do log.info('XXXX') to print in the console
from logging import getLogger

log = getLogger(__name__)


class GetItem(Service):
    def reply(self):

        key = self.request.get("TaskID")
        log.info(key)
        utility = getUtility(IDownloadToolUtility)
        value = utility.get_item(key)

        log.info('VALUE GET ITEM RETURN')
        log.info(value)

        self.request.response.setStatus(200)
        return value
