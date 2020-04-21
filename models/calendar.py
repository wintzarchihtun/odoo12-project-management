from odoo import models,fields,api,_

class MeetingInherit(models.Model):
    _inherit = 'calendar.event'

    patient_name = fields.Char(string="Patient Name")


class EventTypeInherit(models.Model):
    _inherit = 'calendar.event.type'


class AlarmInherit(models.Model):
    _inherit = 'calendar.alarm'


class ManagerInherit(models.AbstractModel):
    _inherit = 'calendar.alarm_manager'


class AttendeeInherit(models.Model):
    _inherit = 'calendar.attendee'