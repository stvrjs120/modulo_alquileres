# -*- coding: utf-8 -*-
from odoo import http

# class ModuloAlquileres(http.Controller):
#     @http.route('/modulo_alquileres/modulo_alquileres/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_alquileres/modulo_alquileres/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_alquileres.listing', {
#             'root': '/modulo_alquileres/modulo_alquileres',
#             'objects': http.request.env['modulo_alquileres.modulo_alquileres'].search([]),
#         })

#     @http.route('/modulo_alquileres/modulo_alquileres/objects/<model("modulo_alquileres.modulo_alquileres"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_alquileres.object', {
#             'object': obj
#         })