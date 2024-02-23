from krita import *
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit
import glob

class LabelIMGExt(Extension):
    def __init__(self,parent):
        super().__init__(parent)
    
    def setup(self):
        pass
    
    def createActions(self,window):
        global goLeftAction
        global goRightAction
        goRightAction = window.createAction("go_right","Go Right")
        goRightAction.triggered.connect(self.dogoRight)
        goLeftAction = window.createAction("go_left","Go Left")
        goLeftAction.triggered.connect(self.dogoLeft)
    
    def dogoLeft(self):
        global idx
        Krita.instance().activeDocument().setBatchmode(True)
        Krita.instance().activeDocument().saveAs(label_list[idx])
        Krita.instance().activeDocument().close()
        if idx > 0:
            idx -= 1
        imgDocument = Krita.instance().openDocument(img_list[idx])
        Krita.instance().activeWindow().addView(imgDocument)
        root_node = Krita.instance().activeDocument().rootNode()
        new_layer = Krita.instance().activeDocument().createNode(label_list[idx].split("\\")[-1],"paintlayer")
        root_node.addChildNode(new_layer,root_node.childNodes()[0])
        labelDocument = Krita.instance().openDocument(label_list[idx])
        width = labelDocument.width()
        height = labelDocument.height()
        label = labelDocument.pixelData(0,0,width,height)
        new_layer.setPixelData(label,0,0,width,height)
        #semi-refresh
        root_node = Krita.instance().activeDocument().rootNode()
        null_layer = Krita.instance().activeDocument().createNode("NULL","paintLayer")
        root_node.addChildNode(null_layer,root_node.childNodes()[0])
        null_layer.remove()
        ###
        console.setText("Frame: "+str(idx))
        
    def dogoRight(self):
        global idx
        Krita.instance().activeDocument().setBatchmode(True)
        Krita.instance().activeDocument().saveAs(label_list[idx])
        Krita.instance().activeDocument().close()
        if idx < len(img_list)-1:
            idx += 1
        imgDocument = Krita.instance().openDocument(img_list[idx])
        Krita.instance().activeWindow().addView(imgDocument)
        root_node = Krita.instance().activeDocument().rootNode()
        new_layer = Krita.instance().activeDocument().createNode(label_list[idx].split("\\")[-1],"paintlayer")
        root_node.addChildNode(new_layer,root_node.childNodes()[0])
        labelDocument = Krita.instance().openDocument(label_list[idx])
        width = labelDocument.width()
        height = labelDocument.height()
        label = labelDocument.pixelData(0,0,width,height)
        new_layer.setPixelData(label,0,0,width,height)
        #semi-refresh
        root_node = Krita.instance().activeDocument().rootNode()
        null_layer = Krita.instance().activeDocument().createNode("NULL","paintLayer")
        root_node.addChildNode(null_layer,root_node.childNodes()[0])
        null_layer.remove()
        ###
        console.setText("Frame: "+str(idx))

class LabelIMGDocker(DockWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Label IMG")
        self.UIElements()
        
    def UIElements(self):
        self.setWidget(widget)
        
    def canvasChanged(self,canvas):
        pass

def setup():
    global idx
    global img_list
    global label_list
    idx = 0
    img_list = glob.glob(img_path_inp.text()+"/*")
    label_list = glob.glob(label_path_inp.text()+"/*")
    Krita.instance().activeDocument().close()
    imgDocument = Krita.instance().openDocument(img_list[0])
    Krita.instance().activeWindow().addView(imgDocument)
    root_node = Krita.instance().activeDocument().rootNode()
    new_layer = Krita.instance().activeDocument().createNode(label_list[0].split("\\")[-1],"paintlayer")
    root_node.addChildNode(new_layer,root_node.childNodes()[0])
    labelDocument = Krita.instance().openDocument(label_list[0])
    width = labelDocument.width()
    height = labelDocument.height()
    label = labelDocument.pixelData(0,0,width,height)
    new_layer.setPixelData(label,0,0,width,height)
    #semi-refresh
    root_node = Krita.instance().activeDocument().rootNode()
    null_layer = Krita.instance().activeDocument().createNode("NULL","paintLayer")
    root_node.addChildNode(null_layer,root_node.childNodes()[0])
    null_layer.remove()
    ###
    console.setText("Frame: "+str(idx))

def goLeft():
    goLeftAction.trigger()

def goRight():
    goRightAction.trigger()

idx = 0
img_list = []
label_list = []

widget = QWidget()
layout = QVBoxLayout()
layout.setAlignment(QtCore.Qt.AlignTop)
img_path_label = QLabel("Image Folder:")
layout.addWidget(img_path_label)
img_path_inp = QLineEdit()
layout.addWidget(img_path_inp)
label_path_label = QLabel("Label Folder:")
layout.addWidget(label_path_label)
label_path_inp = QLineEdit()
layout.addWidget(label_path_inp)
button = QPushButton("SETUP")
button.clicked.connect(setup)
layout.addWidget(button)
right = QPushButton(">>>")
right.clicked.connect(goRight)
layout.addWidget(right)
left = QPushButton("<<<")
left.clicked.connect(goLeft)
layout.addWidget(left)
console = QLabel("Frame: 0")
layout.addWidget(console)
widget.setLayout(layout)
