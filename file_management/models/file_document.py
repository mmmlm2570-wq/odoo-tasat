from odoo import api, fields, models


class FileManagementDocument(models.Model):
    _name = 'file.management.document'
    _description = 'Managed File'
    _order = 'document_date desc, create_date desc, id desc'
    _rec_name = 'name'

    name = fields.Char(string='اسم الملف', required=True, index=True)
    description = fields.Text(string='وصف مختصر')
    category_id = fields.Many2one(
        'file.management.category',
        string='تصنيف الملف',
        required=True,
        ondelete='restrict',
        index=True,
    )
    file_data = fields.Binary(string='رفع الملف أو المرفق', required=True, attachment=True)
    file_name = fields.Char(string='اسم المرفق', required=True)
    document_date = fields.Date(string='تاريخ الملف', required=True, default=fields.Date.context_today, index=True)
    notes = fields.Text(string='ملاحظات')
    uploaded_by = fields.Many2one(related='create_uid', string='أضافه', readonly=True)
    uploaded_on = fields.Datetime(related='create_date', string='تاريخ الرفع', readonly=True)

    @api.onchange('file_data')
    def _onchange_file_data(self):
        if not self.file_data:
            self.file_name = False

