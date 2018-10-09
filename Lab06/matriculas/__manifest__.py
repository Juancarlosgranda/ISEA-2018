# -*- coding: utf-8 -*-
{
    'name': "matriculas",

    'summary': """
        Permite gestionar las matrículas de un centros estudiantiles""",

    'description': """
        Este modulo permite gestionar las matriculas de universidades o institutos.
    """,

    'author': "Grandaports",
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
        'views/alumnos.xml',
        'views/cursos.xml',
        'views/area.xml',
        'views/matriculas.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
}
