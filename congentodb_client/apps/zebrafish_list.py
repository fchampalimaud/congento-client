from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget
from ..models import Zebrafish



class ZebrafishListApp(ModelAdminWidget):

    UID = 'congento-zebrafish'
    MODEL = Zebrafish
    TITLE = 'Congento zebrafish'


    #LIST_FILTER = ['species', 'mta']

    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU = 'middle-left'
    ORQUESTRA_MENU_ORDER = 10
    ORQUESTRA_MENU_ICON = 'database'