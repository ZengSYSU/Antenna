# -*- coding: utf-8 -*-
from win32com import client
import os


class HFSS:
    def __init__(self):
        self.oAnsoftApp = client.Dispatch('AnsoftHFSS.ElectronicsDesktop')
        self.oDesktop = self.oAnsoftApp.GetAppDesktop()
        self.oProject = self.oDesktop.NewProject()
        self.oProject.InsertDesgin('HFSS', 'HFSSDesign1', 'DrivenModal1', '')
        self.oDesign = self.oProject.SetActiveDesign("HFSSDesign1")
        self.oEditor = self.oDesign.SetActiveEditor("3D Modeler")
        self.oModule = self.oDesign.GetModule('BoundarySetup')

    def set_variable(self, _var_name, _var_value):
        _NAME = 'NAME:' + _var_name
        _VALUE = str(_var_value) + 'mm'
        self.oDesign.ChangeProperty(
            ["NAME:AllTabs",
             ["NAME:ProjectVariableTab",
              ["NAME:PropServers", "ProjectVariables"],
              ["NAME:NewProps",
               [_NAME, "PropType:=", "VariableProp", "UserDef:=", True, "Value:=", _VALUE]]]])

    def create_box(self, _xp, _yp, _zp_x, _y ,_z, _name):
        self.oEditor.CreateBox(
            [
                "NAME:BoxParameters",
                "XPosition:=", "-" + _xp + "/2",
                "YPosition:=", "-" + _yp + "/2",
                "ZPosition:=", "0mm",
                "XSize:=", _x,
                "YSize:=", _y,
                "ZSize:=", _z,
            ],
            [
                "NAME:Attributes",
                "Name:=", _name,
                "Flags:=", "",
                "Color:=", "(143 175 143)",
                "Transparency:=", 0,
                "PartCoordinateSystem:=", "Global",
                "UDMId:=", "",
                "MaterialValue:=", "\"FR4_epoxy\"",
                "SurfaceMaterialValue:=", "\"\"",
                "SolveInside:=", True,
                "IsMaterialEditable:=", True,
                "UseMaterialAppearance:=", False
            ])

    def create_rectangle(self, _rxp, _ryp, _rzp, _rx, _ry, _name, _axis):
        self.oEditor.CreateRectangle(
            [
                "NAME:RectangleParameters",
                "IsCovered:=", True,
                "XStart:=", "-" + _rxp + "/2",
                "YStart:=", "-" + _ryp + "/2",
                "ZStart:="	, _rzp,
                "Width:="		, _rx,
                "Height:="		, _ry,
                "WhichAxis:="		, _axis
            ],
            [
                "NAME:Attributes",
                "Name:="		, _name,
                "Flags:="		, "",
                "Color:="		, "(143 175 143)",
                "Transparency:="	, 0,
                "PartCoordinateSystem:=", "Global",
                "UDMId:="		, "",
                "MaterialValue:="	, "\"vacuum\"",
                "SurfaceMaterialValue:=", "\"\"",
                "SolveInside:="		, True,
                "IsMaterialEditable:="	, True,
                "UseMaterialAppearance:=", False
            ])

    def mirror(self, _obj, bx, by, bz, nx, ny, nz):
        self.oEditor.DuplicateMirror(
            [
                "NAME:Selections",
                "Selections:="	, _obj,
                "NewPartsModelFlag:="	, "Model"
            ],
            [
                "NAME:DuplicateToMirrorParameters",
                "DuplicateMirrorBaseX:=", bx,
                "DuplicateMirrorBaseY:=", by,
                "DuplicateMirrorBaseZ:=", bz,
                "DuplicateMirrorNormalX:=", nx,
                "DuplicateMirrorNormalY:=", ny,
                "DuplicateMirrorNormalZ:=", nz
            ],
            [
                "NAME:Options",
                "DuplicateAssignments:=", False
            ],
            [
                "CreateGroupsForNewObjects:=", False
            ])

    def subtract(self, _obj1, _obj2):
        self.oEditor.Subtract(
            [
                "NAME:Selections",
                "Blank Parts:="	, _obj1,
                "Tool Parts:="		, _obj2
            ],
            [
                "NAME:SubtractParameters",
                "KeepOriginals:=", False
            ]
        )

    def set_material(self,_obj, _mat):
        self.oEditor.AssignMaterial(
            [
                "NAME:Selections",
                "AllowRegionDependentPartSelectionForPMLCreation:=", True,
                "AllowRegionSelectionForPMLCreation:=", True,
                "Selections:=", _obj
            ],
            [
                "NAME:Attributes",
                "MaterialValue:=", "\"" + _mat + "\"",
                "SolveInside:="	, False,
                "IsMaterialEditable:="	, True,
                "UseMaterialAppearance:=", False
            ])

    def