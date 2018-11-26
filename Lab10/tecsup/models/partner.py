# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Partner(models.Model):
     _inherit = 'res.partner'

     instructor = fields.Boolean('instructor',default=False)
     session_ids = fields.Many2many('openacademy.session',string='Attended sessions',readonly=True)
