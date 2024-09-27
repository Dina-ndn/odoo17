# -*- coding: utf-8 -*-
{
    'name': "Waaneiza File Upload",

    'summary': """
        This is waaneiza file upload module.""",

    'description': """
        Customerized module for file upload. Created for Waaneiza World Wide.
    """,

    'author': "Swe Zin Lynn Lett",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
     'depends': ['base','mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/file_upload_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}