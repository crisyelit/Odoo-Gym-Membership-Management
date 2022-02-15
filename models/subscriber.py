# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta, datetime

class Subscriber(models.Model):
    _name = 'gym.subscriber'
    _sql_constraints = [('unique_mail', 'unique(email)', 'This email already exists')]

    name = fields.Char(string = 'Name', required = True)
    id_number = fields.Char(string = 'ID Number', required = True)
    address = fields.Text(string = 'Address')
    phone = fields.Char(string = 'Phone number')
    email = fields.Char(string = 'Email', required = True)

    start_date = fields.Datetime(string='Start date', required=True)
    duration = fields.Integer(string='Duration (Weeks)', required=True)
    end_date = fields.Datetime(string="End date", store=True, compute='_get_end_date')

    membership_state = fields.Char(string="Membership State", store=True, compute='_get_state')
    membership_id = fields.Many2one('gym.membership', ondelete='restrict', string='Membership', required = True)

    activity_id = fields.Many2one('gym.activity', ondelete='restrict', string='Activity', required = True)

    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for r in self:
            if r.duration and r.start_date:
                duration = timedelta(weeks=r.duration)
                r.end_date = r.start_date + duration

    @api.depends('end_date')
    def _get_state(self):
        for r in self:
            if r.end_date and datetime.now() > r.end_date :
                    r.membership_state = 'Expired'
            elif r.end_date and datetime.now() < r.end_date :
                    r.membership_state = 'Valide'