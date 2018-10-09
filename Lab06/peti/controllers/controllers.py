# -*- coding: utf-8 -*-
from odoo import http

# class Peti(http.Controller):
#     @http.route('/peti/peti/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/peti/peti/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('peti.listing', {
#             'root': '/peti/peti',
#             'objects': http.request.env['peti.peti'].search([]),
#         })

#     @http.route('/peti/peti/objects/<model("peti.peti"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('peti.object', {
#             'object': obj
#         })