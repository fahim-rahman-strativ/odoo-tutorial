from odoo import fields, models

class EstateProperty(models.Model):
    # _name = "inherited.model"
    # _description = "Inherited Model"
    _inherit = "estate.property"

    # property_ids = fields.One2many('estate.property', string='Property ID')
    property_ids = fields.One2many('estate.property', 'user_id')