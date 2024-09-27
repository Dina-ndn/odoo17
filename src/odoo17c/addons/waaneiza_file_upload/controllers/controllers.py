# -*- coding: utf-8 -*-
# from odoo import http


# class WaaneizaFileUpload(http.Controller):
#     @http.route('/waaneiza_file_upload/waaneiza_file_upload', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/waaneiza_file_upload/waaneiza_file_upload/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('waaneiza_file_upload.listing', {
#             'root': '/waaneiza_file_upload/waaneiza_file_upload',
#             'objects': http.request.env['waaneiza_file_upload.waaneiza_file_upload'].search([]),
#         })

#     @http.route('/waaneiza_file_upload/waaneiza_file_upload/objects/<model("waaneiza_file_upload.waaneiza_file_upload"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('waaneiza_file_upload.object', {
#             'object': obj
#         })
