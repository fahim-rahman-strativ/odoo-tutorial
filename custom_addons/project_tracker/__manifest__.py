{
    'name': 'Project Tracker',
    'version': '1.0',
    'summary': 'A simple project management module',
    'author': 'Fahim',
    'category': 'Project',
    'depends': ['base'],
    'data': [
        'views/project_tracker_views.xml',
        'views/project_tracker_menu.xml',
        'security/ir.model.access.csv',
        'security/project_tracker_security.xml',
    ],
    'installable': True,
    'application': True,
}