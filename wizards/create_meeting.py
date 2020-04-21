from odoo import models, fields, api, _


class CreateMeeting(models.Model):
    _name="create.meeting"
    _description="for create meeting"

    def _get_default_participant(self):
        result = []
        result.append(self.env.user.id)
        return [(6, 0, result)]
    name=fields.Char(string="Meeting Name")
    date_delay = fields.Float('Duration', required=True, default=1.0)
    meeting_date = fields.Datetime(string="Meeting Date")
    participants = fields.Many2many('res.users', string='Participant', required=True,default=_get_default_participant)

    def create_appointment(self):
        vals = {
            'name':self.name,
            'date_delay':self.date_delay,
            'participants': self.participants,
            'date': self.meeting_date,
            'notes': 'Created From The Wizard/Code'
        }
        # adding a message to the chatter from code
        # self.patient_id.message_post(body="Test string ", subject="Appointment Creation")
        # creating appointments from the code

        self.env['sinerkia_jitsi_meet.jitsi_meet'].create(vals)

        # context['form_view_initial_mode']='edit'
        #



