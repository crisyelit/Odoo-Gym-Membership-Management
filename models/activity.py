# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Activity(models.Model):
    _name = 'gym.activity'

    name = fields.Char(compute = '_full_name',default="MemberShip")
    title = fields.Char(string = 'Name', required = True)
    description = fields.Text(string = 'Description')
    subscriber_ids = fields.One2many('gym.subscriber', 'activity_id', string = 'Subscribers')

    @api.depends('title')
    def _full_name(self):
        for r in self:
            if r.title:
                r.name = r.title
