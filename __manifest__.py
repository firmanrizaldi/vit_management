# -*- coding: utf-8 -*-
{
    'name': "vit_management",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "firmanrizaldiyusup@gmail.com",
    'website': "www.vitraining.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/perangkat_dc.xml' ,
        'views/perangkat_dc_util.xml' ,
        'views/maintenances.xml' ,
        'views/power_dis.xml' ,
        'views/capacity.xml' ,
        'views/rekruitment.xml' ,
        'views/sop.xml' ,
        'views/bcp.xml' ,
        'views/berita.xml' ,
        'views/agenda.xml' ,
        'views/data_user.xml' ,
        'views/lokasi.xml' ,
        'views/ruang.xml' ,
        'views/sub_ruang.xml' ,
        'views/merek.xml' ,
        'views/unit.xml' ,
        'sequence/squence.xml' ,
    ],
    "installable": True,
    "auto_install": False,
    "application": True,

}