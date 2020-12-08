# -*- coding: utf-8 -*-
from win32com import client
import os


class HFSS:
    def __init__(self):
        self.oAnsoftApp = client.Dispatch('AnsoftHfss.HfssScriptInterface')
        self.oDesktop = self.oAnsoftApp.GetAppDesktop()
        self.oProject = self.oDesktop.NewProject()
        self.oProject.InsertDesign('HFSS', 'HFSSDesign1', 'DrivenModal1', '')
        self.oDesign = self.oProject.SetActiveDesign("HFSSDesign1")
        self.oEditor = self.oDesign.SetActiveEditor("3D Modeler")
        self.oModule = self.oDesign.GetModule('BoundarySetup')
        self.transparency = 0.5

    def set_variable(self, _var_name, _var_value):
        _NAME = 'NAME:' + _var_name
        _VALUE = str(_var_value) + 'mm'
        self.oDesign.ChangeProperty(["NAME:AllTabs",
                                     ["NAME:LocalVariableTab",
                                      ["NAME:PropServers", "LocalVariables"],
                                      ["NAME:NewProps",
                                       [_NAME, "PropType:=", "VariableProp", "UserDef:=", True, "Value:=", _VALUE]]]])

    def create_centered_rectangle(self, _var_x, _var_y, _var_z, _name, _dir='Z'):
        self.oEditor.CreateRectangle(
            [
                "NAME:RectangleParameters",
                "IsCovered:=", True,
                "XStart:="	, '-' + _var_x + '/2',
                "YStart:="		, '-' + _var_y + '/2',
                "ZStart:="		, _var_z,
                "Width:="		, _var_x,
                "Height:="		, _var_y,
                "WhichAxis:="		, _dir
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

    def connect(self, _obj1, _obj2):
        self.oEditor.Connect(["NAME:Selections", "Selections:=", _obj1 + ',' + _obj2])

    def unite(self, _obj1, _obj2):
        self.oEditor.Unite(["NAME:Selections", "Selections:=", _obj1 + ',' + _obj2],
                           ["NAME:UniteParameters", "KeepOriginals:=", False])

    def subtract(self, _obj1, _obj2):
        self.oEditor.Subtract(["NAME:Selections", "Blank Parts:=", _obj1, "Tool Parts:=", _obj2],
                              ["NAME:SubtractParameters", "KeepOriginals:=", False])

    def copy_and_paste(self, _obj):
        self.oEditor.Copy(["NAME:Selections", "Selections:=", _obj])
        self.oEditor.Paste()

    def set_material(self, _obj, _mat='pec'):
        self.oEditor.AssignMaterial(
            [
                "NAME:Selections",
                "AllowRegionDependentPartSelectionForPMLCreation:=", True,
                "AllowRegionSelectionForPMLCreation:=", True,
                "Selections:="	, _obj
            ],
            [
                "NAME:Attributes",
                "MaterialValue:="	, "\"" + _mat + "\"",
                "SolveInside:="		, False,
                "IsMaterialEditable:="	, True,
                "UseMaterialAppearance:=", False
            ])

    def assign_port(self, _obj):
        self.oModule.AssignWavePort(["NAME:1", "Objects:=", [_obj],
                                     "NumModes:=", 1, "RenormalizeAllTerminals:=", True,
                                     "UseLineModeAlignment:=", False, "DoDeembed:="	, False,
                                     ["NAME:Modes",
                                      ["NAME:Mode1", "ModeNum:=", 1, "UseIntLine:=", False, "CharImp:=", "Zpi"]],
                                     "ShowReporterFilter:="	, False,
                                     "ReporterFilter:="	, [True],
                                     "UseAnalyticAlignment:=", False])

    def create_region(self, _var_ab):
        self.oEditor.CreateRegion(
            [
                "NAME:RegionParameters",
                "+XPaddingType:="	, "Absolute Offset",
                "+XPadding:="		, _var_ab,
                "-XPaddingType:="	, "Absolute Offset",
                "-XPadding:="		, _var_ab,
                "+YPaddingType:="	, "Absolute Offset",
                "+YPadding:="		, _var_ab,
                "-YPaddingType:="	, "Absolute Offset",
                "-YPadding:="		, _var_ab,
                "+ZPaddingType:="	, "Absolute Offset",
                "+ZPadding:="		, _var_ab,
                "-ZPaddingType:="	, "Absolute Offset",
                "-ZPadding:="		, _var_ab
            ],
            [
                "NAME:Attributes",
                "Name:="		, "Region",
                "Flags:="		, "Wireframe#",
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

    def assign_radiation_region(self):
        self.oModule.AssignRadiation(
            [
                "NAME:Rad1",
                "Objects:="		, ["Region"],
                "IsFssReference:="	, False,
                "IsForPML:="		, False
            ])

    def insert_radiation_setup(self):
        mod = self.oDesign.GetModule('RadField')
        mod.InsertFarFieldSphereSetup(
            [
                "NAME:Infinite Sphere1",
                "UseCustomRadiationSurface:=", False,
                "ThetaStart:="		, "-180deg",
                "ThetaStop:="		, "180deg",
                "ThetaStep:="		, "1deg",
                "PhiStart:="		, "0deg",
                "PhiStop:="		, "90deg",
                "PhiStep:="		, "90deg",
                "UseLocalCS:="		, False
            ])

    def insert_analysis_setup(self, _freq):
        mod = self.oDesign.GetModule('AnalysisSetup')
        mod.InsertSetup("HfssDriven",
        [
            "NAME:Setup1",
            "AdaptMultipleFreqs:="	, False,
            "Frequency:="		, str(_freq) + 'GHz',
            "MaxDeltaS:="		, 0.02,
            "PortsOnly:="		, False,
            "UseMatrixConv:="	, False,
            "MaximumPasses:="	, 20,
            "MinimumPasses:="	, 1,
            "MinimumConvergedPasses:=", 1,
            "PercentRefinement:="	, 30,
            "IsEnabled:="		, True,
            "BasisOrder:="		, 1,
            "DoLambdaRefine:="	, True,
            "DoMaterialLambda:="	, True,
            "SetLambdaTarget:="	, False,
            "Target:="		, 0.3333,
            "UseMaxTetIncrease:="	, False,
            "PortAccuracy:="	, 2,
            "UseABCOnPort:="	, False,
            "SetPortMinMaxTri:="	, False,
            "UseDomains:="		, False,
            "UseIterativeSolver:="	, False,
            "SaveRadFieldsOnly:="	, False,
            "SaveAnyFields:="	, True,
            "IESolverType:="	, "Auto",
            "LambdaTargetForIESolver:=", 0.15,
            "UseDefaultLambdaTgtForIESolver:=", True
        ])

    def create_reports(self):
        mod = self.oDesign.GetModule('ReportSetup')
        mod.CreateReport("VSWR Plot 1", "Modal Solution Data", "Rectangular Plot", "Setup1 : LastAdaptive", [],
                         ["Freq:=", ["All"], ],
                         ["X Component:=", "Freq",
                          "Y Component:=", ["VSWR(1)"]], [])

        mod.CreateReport("Realized Gain Plot 1", "Far Fields", "Rectangular Plot", "Setup1 : LastAdaptive",
                         ["Context:=", "Infinite Sphere1"],
                         [
                            "Theta:="		, ["All"],
                            "Phi:="			, ["All"],
                            "Freq:="		, ["All"],
                         ],
                         [
                            "X Component:="		, "Theta",
                            "Y Component:="		, ["dB(RealizedGainTotal)"]
                         ], [])
        mod.AddTraceCharacteristics("Realized Gain Plot 1", "max", [], ["Full"])
        mod.AddTraceCharacteristics("Realized Gain Plot 1", "xdb10Beamwidth", ["3"], ["Full"])

    def save_prj(self):
        _base_path = os.getcwd()
        _prj_num = 1
        while True:
            _path = os.path.join(_base_path, 'Prj{}.aedt'.format(_prj_num))
            if os.path.exists(_path):
                _prj_num += 1
            else:
                break
        self.oProject.SaveAs(_path, True)

    def run(self):
        self.oDesktop.RestoreWindow()
        self.oDesign.Analyze('Setup1')
