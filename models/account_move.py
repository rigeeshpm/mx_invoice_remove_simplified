from odoo import models

class MxAccountMove(models.Model):
    _inherit = 'account.move'

    def _l10n_gcc_get_invoice_title(self):
        self.ensure_one()
        if self.company_id.country_code != 'AE':
            return super()._l10n_gcc_get_invoice_title()

        # Override: always return 'Tax Invoice' even for simplified
        return self.env._('Invoice')
