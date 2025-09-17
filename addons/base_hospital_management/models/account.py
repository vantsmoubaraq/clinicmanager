from odoo import models, fields, api

class MyAccountMove(models.Model):
    _name = "my.account.move"          # new model
    _description = "My Account Move"
    _inherits = {"account.move": "move_id"}  # delegated inheritance

    move_id = fields.Many2one(
        "account.move", 
        required=True, 
        ondelete="cascade"
    )
