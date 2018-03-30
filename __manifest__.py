# -*- coding: utf-8 -*-
{
    'name': "Default Product Taxes",

    'summary': """
        Set default taxes values to your products""",

    'description': """
        This module is useful if you have many companies or different taxes for the same product and company

        Is devised to have multiple companies, so will put the company of product and partner as empty value
    """,

    'author': "Sergio del Castillo Baranda",
    'website': "http://www.sergiodelcastillo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale','purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/record_tax.xml',
        'views/default_taxes_views.xml',
    ],
}