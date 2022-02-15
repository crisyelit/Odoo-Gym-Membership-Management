# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Membership(models.Model):
    _name = 'gym.membership'

    name = fields.Char(compute = '_full_name',default="MemberShip")
    title = fields.Char(string = 'Name', required = True)
    description = fields.Text(string = 'Description')
    price = fields.Char(string = 'Price', required = True)
    subscriber_ids = fields.One2many('gym.subscriber', 'membership_id', string = 'Subscribers')

    @api.depends('title')
    def _full_name(self):
        for r in self:
            if r.title:
                r.name = r.title
