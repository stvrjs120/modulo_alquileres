# -*- coding: utf-8 -*-
from odoo import fields, models

class Partner(models.Model):
    _inherit = 'res.partner'

    cliente = fields.Char(string="Cliente", required=True)

    local_ids = fields.Many2many('modulo_alquileres.local', string="Locales Alquilados", readonly=True)