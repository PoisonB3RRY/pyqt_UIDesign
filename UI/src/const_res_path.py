import os


class ResPath():

    RES_PATH = os.path.dirname(os.path.dirname(__file__)) + '\\res'
    SPDB_ICON_PATH = RES_PATH + '\\spdb_logo.svg'
    SUCCESS_ICON_PATH = RES_PATH + '\\success.svg'
    FAILED_ICON_PATH = RES_PATH + '\\failed.svg'
    READY_ICON_PATH = RES_PATH + '\\ready.svg'
    NEED_ICON_PATH = RES_PATH + '\\need.svg'

