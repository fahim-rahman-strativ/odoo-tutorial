# -*- coding: utf-8 -*-

from odoo import models, fields

class ProjectTracker(models.Model):
    _name = 'project.tracker'
    _description = 'Project Tracker'

    name = fields.Char(string='Project Name', required=True)
    description = fields.Text(string='Description')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    user_id = fields.Many2one('res.users', string='Assigned To')
    status = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ], string='Status', default='new')