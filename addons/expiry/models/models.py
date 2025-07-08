# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class expiry(models.Model):
#     _name = 'expiry.expiry'
#     _description = 'expiry.expiry'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import models, fields, api
from datetime import datetime, timedelta

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    expiry_date = fields.Date(string="Expiry Date")

    @api.model
    def check_expiry_dates(self):
        today = datetime.today().date()
        notification_period = timedelta(days=7)

        # Find products that are within the notification period or expired
        expiring_products = self.search([
            ('expiry_date', '!=', False),
            ('expiry_date', '<=', today + notification_period)
        ])

        for product in expiring_products:
            # Create the message content
            message = f"Product '{product.name}' is expiring on {product.expiry_date}."

            # Send an internal notification to specific users (e.g., all users in a specific group)
            # You can specify user IDs, or get the list of users dynamically

            user_group = self.env.ref('base.group_user')  # Replace with the correct group reference
            for user in user_group.users:
                # Send internal notification
                self.env['mail.message'].create({
                    'message_type': 'notification',
                    'subtype_id': self.env.ref('mail.mt_comment').id,
                    'body': message,
                    'subject': 'Product Expiry Notification',
                    'partner_ids': [(4, user.partner_id.id)],
                    'model': 'product.template',
                    'res_id': product.id,  # Link notification to the product record
                })
