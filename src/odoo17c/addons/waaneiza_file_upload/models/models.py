# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class waaneiza_file_upload(models.Model):
#     _name = 'waaneiza_file_upload.waaneiza_file_upload'
#     _description = 'waaneiza_file_upload.waaneiza_file_upload'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
