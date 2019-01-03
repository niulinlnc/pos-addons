import odoo.tests


@odoo.tests.common.at_install(True)
@odoo.tests.common.post_install(True)
class TestUi(odoo.tests.HttpCase):

    def test_01_pos_is_loaded(self):
        # see more https://odoo-development.readthedocs.io/en/latest/dev/tests/js.html#phantom-js-python-tests
        env = self.env

        # get exist pos_config
        main_pos_config = env.ref('point_of_sale.pos_config_main')
        # create new session and open it
        main_pos_config.open_session_cb()

        env['ir.module.module'].search([('name', '=', 'pos_mobile')], limit=1).state = 'installed'

        self.phantom_js(
            '/pos/web?m=1',

            "odoo.__DEBUG__.services['web_tour.tour']"
            ".run('pos_mobile_tour')",

            "odoo.__DEBUG__.services['web_tour.tour']"
            ".tours.pos_mobile_tour.ready",

            login="admin",
            timeout=1000,
        )
