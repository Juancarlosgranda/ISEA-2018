# -*- coding: utf-8 -*-
{
    'name': "PETI",

    'summary': """
        Modulo para gestionar proyectos de software""",

    'description': """
        Gestion de proyectos de software para un mayor control.
    """,

    'author': "Granda",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/proyectos.xml',
        'views/actividades.xml',
        'views/detalles.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
}
