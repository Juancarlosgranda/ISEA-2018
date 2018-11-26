# -*- coding: utf-8 -*-
from odoo import http

# class Tecsup(http.Controller):
#     @http.route('/tecsup/tecsup/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tecsup/tecsup/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tecsup.listing', {
#             'root': '/tecsup/tecsup',
#             'objects': http.request.env['tecsup.tecsup'].search([]),
#         })

#     @http.route('/tecsup/tecsup/objects/<model("tecsup.tecsup"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tecsup.object', {
#             'object': obj
#         })