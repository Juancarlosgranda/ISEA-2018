# -*- coding: utf-8 -*-
from odoo import http

class Tecsup(http.Controller):
     @http.route('/academy/academy/', auth='public', website=True)
     def index(self, **kw):
         Session = http.request.env['openacademy.session']
         return http.request.render('tecsup.index',{
             'sessions': Session.search([])
         })

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