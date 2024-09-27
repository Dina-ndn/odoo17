from odoo import models,fields

class FileUpload(models.Model):
	_name = "file.upload"
	_inherit = ['mail.thread', 'mail.activity.mixin']
	_description = "File Upload"
	_rec_name = "file_name"

	file_name = fields.Char(string="File Name",tracking=True)
	employee_name = fields.Char(string="Employee Name",tracking=True)
	form_link = fields.Char(string="Form Link",tracking=True)
	upload_survey = fields.Binary(string="Upload Survey File",attachment=False,store=True)
	survey_name = fields.Char(string="Survey File Name")
	upload_report = fields.Binary(string="Upload Report File",attachment=False,store=True)
	report_name = fields.Char(string="Report File Name")

	def action_customer(self):
		return {
            'res_model': 'res.partner',
            'type': 'ir.actions.act_window',
            'tag': 'reload',
            'view_mode': 'form',
            'view_type': 'form',
            'view_id': self.env.ref("base.view_partner_form").id,
            'target': 'self.'
        }

	def action_supplier(self):
		return {
            'res_model': 'res.partner',
            'type': 'ir.actions.act_window',
            'tag': 'reload',
            'view_mode': 'form',
            'view_type': 'form',
            'view_id': self.env.ref("base.view_partner_form").id,
            'target': 'self.'
        }

	def action_vendor(self):
		return {
            'res_model': 'res.partner',
            'type': 'ir.actions.act_window',
            'tag': 'reload',
            'view_mode': 'form',
            'view_type': 'form',
            'view_id': self.env.ref("base.view_partner_form").id,
            'target': 'self.'
        }






