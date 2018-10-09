# -*- coding: utf-8 -*-
from odoo import http

# class Matriculas(http.Controller):
#     @http.route('/matriculas/matriculas/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/matriculas/matriculas/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('matriculas.listing', {
#             'root': '/matriculas/matriculas',
#             'objects': http.request.env['matriculas.matriculas'].search([]),
#         })

#     @http.route('/matriculas/matriculas/objects/<model("matriculas.matriculas"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('matriculas.object', {
#             'object': obj
#         })