import os
import sys

__all__ = [ "PW_DRIVE", "PW_DIR", "PW_WIDGETS_DIR", "PWCFG" ]

PW_DRIVE = r"d:"
PW_DIR = os.path.join(PW_DRIVE,r"\projetos\pys60\pys60widgets")
PW_WIDGETS_DIR = os.path.join(PW_DIR,r"widgets")

class PWidgetCfg(object):
    def __init__(self):
        sys.path.insert(0,PW_WIDGETS_DIR)
        sys.path.insert(0,PW_DIR)

PWCFG = PWidgetCfg()
