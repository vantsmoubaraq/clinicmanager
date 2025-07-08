# -*- coding: utf-8 -*-
# from odoo import http


# class Expiry(http.Controller):
#     @http.route('/expiry/expiry', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/expiry/expiry/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('expiry.listing', {
#             'root': '/expiry/expiry',
#             'objects': http.request.env['expiry.expiry'].search([]),
#         })

#     @http.route('/expiry/expiry/objects/<model("expiry.expiry"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('expiry.object', {
#             'object': obj
#         })
