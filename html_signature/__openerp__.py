# -*- coding: utf-8 -*-
{
    "name" : "CITEC Plugins - HTML Signature",
    "version" : "1.0",
    "author" : "Grupo CITEC",
    "category": 'CITEC Plugins',
    'complexity': "easy",
    "description": """
CITEC Plugins - HTML Signature
====================================
This modules enables HTML signature in user preferences

for OpenERP 7.0

Programado pelo Grupo CITEC Ltda.
v2.0

dummy change
    """,
    'website': 'http://www.grupocitec.com',
    "depends" : [
    	"base", 
    	"mail", 
	],
    'init_xml': [],
    'update_xml': [
    	'view/res_users_view.xml',
    ],
    'demo_xml': [],
    'test': [],
    'application': False,
    'installable': True,
    'css': [
    ],
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
