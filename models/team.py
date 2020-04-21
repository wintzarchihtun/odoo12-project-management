from odoo import models, fields, api, _


class Team(models.Model):
    _name = "project.team"
    _description = "for create team"

    name = fields.Char(string="Name")
    description = fields.Text(string="About of Team")


# class File(models.Model):
#     _inherit = 'muk_dms.file'
