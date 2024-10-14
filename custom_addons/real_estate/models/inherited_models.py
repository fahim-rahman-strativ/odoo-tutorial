from odoo import fields, models

class InheritedModel(models.Model):
    _name = "inherited.model"
    _description = "Inherited Model"
    _inherit = "estate.property"

    property_ids = fields.One2many('res.users', string='Property ID')
