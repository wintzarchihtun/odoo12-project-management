from odoo import models, fields, api, _


class Meeting(models.Model):
    _inherit = 'sinerkia_jitsi_meet.jitsi_meet'


class ExternalUser(models.Model):
    _inherit = 'sinerkia_jitsi_meet.external_user'
