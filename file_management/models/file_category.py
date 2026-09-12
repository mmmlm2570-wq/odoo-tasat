from odoo import fields, models


class FileManagementCategory(models.Model):
    _name = 'file.management.category'
    _description = 'File Category'
    _order = 'name'

    name = fields.Char(string='اسم التصنيف', required=True, translate=True)
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ('file_management_category_name_unique', 'unique(name)', 'The category name must be unique.'),
    ]

