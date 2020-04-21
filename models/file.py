from odoo import models


class MyFile(models.Model):
    _inherit = 'muk_dms.file'


class Dictory(models.Model):
    _inherit = 'muk_dms.directory'
