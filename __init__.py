# Copyright (c) 2018 Ultimaker B.V.
# Cura is released under the terms of the LGPLv3 or higher.

from . import BrushSupport

from UM.i18n import i18nCatalog
i18n_catalog = i18nCatalog("cura")

def getMetaData():
    return {
        "tool": {
            "name": i18n_catalog.i18nc("@label", "Brush Support"),
            "description": i18n_catalog.i18nc("@info:tooltip", "Draw and erase areas where support needs to be generated."),
            "icon": "support_brush.svg",
            "tool_panel": "CustomSupportPanel.qml",
            "weight": 9
        }
    }

def register(app):
    return {"tool": BrushSupport.BrushSupport()}