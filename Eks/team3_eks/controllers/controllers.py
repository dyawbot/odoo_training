# -*- coding: utf-8 -*-
from odoo import http

# class Team3Eks(http.Controller):
#     @http.route('/team3_eks/team3_eks/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/team3_eks/team3_eks/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('team3_eks.listing', {
#             'root': '/team3_eks/team3_eks',
#             'objects': http.request.env['team3_eks.team3_eks'].search([]),
#         })

#     @http.route('/team3_eks/team3_eks/objects/<model("team3_eks.team3_eks"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('team3_eks.object', {
#             'object': obj
#         })