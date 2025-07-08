# -*- coding: utf-8 -*-
# from odoo import http


# class Sxpiry(http.Controller):
#     @http.route('/sxpiry/sxpiry', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sxpiry/sxpiry/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sxpiry.listing', {
#             'root': '/sxpiry/sxpiry',
#             'objects': http.request.env['sxpiry.sxpiry'].search([]),
#         })

#     @http.route('/sxpiry/sxpiry/objects/<model("sxpiry.sxpiry"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sxpiry.object', {
#             'object': obj
#         })
