# -*- coding: utf-8 -*-
from odoo import http

# class Convalidaciones(http.Controller):
#     @http.route('/convalidaciones/convalidaciones/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/convalidaciones/convalidaciones/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('convalidaciones.listing', {
#             'root': '/convalidaciones/convalidaciones',
#             'objects': http.request.env['convalidaciones.convalidaciones'].search([]),
#         })

#     @http.route('/convalidaciones/convalidaciones/objects/<model("convalidaciones.convalidaciones"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('convalidaciones.object', {
#             'object': obj
#         })