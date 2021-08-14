import os
from pkg_resources import get_distribution
from ckan import __version__ as ckan_version


def _get_nice_lib(lib_name):
    """ Get lib info
        # TODO add URL https://stackoverflow.com/questions/38659408/how-do-i-get-a-python-distribution-url """

    try:
        res = get_distribution(lib_name).version
    except Exception as e:
        res = 'Error obteniendo datos de {}: {}'.format(lib_name, e)

    return res


def get_ui_uni_info():
    """ Get info about this compilation """
    data = {}
    data['CKAN para Universidades Argentinas versión'] = os.getenv('CKAN_UNI_VERSION')
    data['Versión de CKAN'] = ckan_version
    data['Extensión SIU Harvester'] = _get_nice_lib('ckanext-siu-harvester')
    data[' - pySIUData'] = _get_nice_lib('siu-data')
    data['Extensión Dataset preview'] = _get_nice_lib('ckanext-datasetpreview')

    return data.items()
