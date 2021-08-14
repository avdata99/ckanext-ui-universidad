import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckanext.ui_universidad.helpers import get_ui_uni_info


class UiUniversidadPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'ui_universidad')

    # ITemplateHelpers

    def get_helpers(self):
        return {'ui_uni_system_info': get_ui_uni_info}
