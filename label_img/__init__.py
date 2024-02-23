from .label_img import LabelIMGDocker, LabelIMGExt
from krita import *

Krita.instance().addExtension(LabelIMGExt(Krita.instance()))
Krita.instance().addDockWidgetFactory(DockWidgetFactory("Label IMG",DockWidgetFactoryBase.DockRight,LabelIMGDocker))
