# -*- coding: utf-8 -*-
from odoo import http

# class Etsi-membership(http.Controller):
#     @http.route('/etsi-membership/etsi-membership/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/etsi-membership/etsi-membership/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('etsi-membership.listing', {
#             'root': '/etsi-membership/etsi-membership',
#             'objects': http.request.env['etsi-membership.etsi-membership'].search([]),
#         })

#     @http.route('/etsi-membership/etsi-membership/objects/<model("etsi-membership.etsi-membership"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('etsi-membership.object', {
#             'object': obj
#         })