{
    'name': 'إدارة الملفات',
    'summary': 'إدارة بسيطة للملفات والمرفقات',
    'version': '19.0.1.0.0',
    'category': 'Productivity',
    'author': 'Your Company',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/file_management_security.xml',
        'security/ir.model.access.csv',
        'data/file_category_data.xml',
        'views/file_category_views.xml',
        'views/file_document_views.xml',
        'views/file_management_menus.xml',
    ],
    'application': True,
    'installable': True,
}

