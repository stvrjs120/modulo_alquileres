# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Edificio(models.Model):
    _name = 'modulo_alquileres.edificio'

    nombre_edificio = fields.Char(string="Nombre", required=True)
    direccion_edificio = fields.Char(string="Direccion", required=True)
    area_terrero_edificio = fields.Integer(string="Area Terreno", required=True, help="Metros cuadrados")
    area_construida_edificio = fields.Integer(string="Area Construida", required=True, help="Metros cuadrados")
    valor_real = fields.Float(digits=(12, 2), string="Valor Real", required=True)
    valor_real = fields.Float(digits=(12, 2), string="Valor Real", required=True)

    piso_ids = fields.One2many('modulo_alquileres.piso', 'edificio_id', string="Pisos")


class Piso(models.Model):
    _name = 'modulo_alquileres.piso'

    numero_piso = fields.Integer(string="Número", required=True)

    local_ids = fields.One2many('modulo_alquileres.local', 'piso_id', string="Locales")
    edificio_id = fields.Many2one('modulo_alquileres.edificio', ondelete='cascade', string="Edificio", required=True)


class Local(models.Model):
    _name = 'modulo_alquileres.local'

    numero_local = fields.Integer(string="Número de Local", required=True)
    area_m2 = fields.Integer(string="Área m2", required=True)
    medidor_electrico = fields.Integer(string="Número del Medidor Eléctrico", required=True)
    medidor_agua = fields.Integer(string="Número del Medidor de Agua", required=True)

    piso_id = fields.Many2one('modulo_alquileres.piso', ondelete='cascade', string="Piso", required=True)

    cliente_id = fields.Many2one('res.partner', string="Cliente")

