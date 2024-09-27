# -*- coding: utf-8 -*-
# from odoo import http


# class ProjectTracker(http.Controller):
#     @http.route('/project_tracker/project_tracker', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project_tracker/project_tracker/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('project_tracker.listing', {
#             'root': '/project_tracker/project_tracker',
#             'objects': http.request.env['project_tracker.project_tracker'].search([]),
#         })

#     @http.route('/project_tracker/project_tracker/objects/<model("project_tracker.project_tracker"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project_tracker.object', {
#             'object': obj
#         })
