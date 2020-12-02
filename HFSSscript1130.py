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

    def create_box(self, _xp, _yp, _zp, _x, _y, _z, _name):
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
                "ZStart:=", _rzp,
                "Width:=", _rx,
                "Height:="	, _ry,
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

    def set_material(self, _obj, _mat):
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

    def create_region(self, _fourth):
        self.oEditor.CreateRegion(
            [
                "NAME:RegionParameters",
                "+XPaddingType:=", "Absolute Offset",
                "+XPadding:=", _fourth,
                "-XPaddingType:=", "Absolute Offset",
                "-XPadding:="	, _fourth,
                "+YPaddingType:="	, "Absolute Offset",
                "+YPadding:="		, _fourth,
                "-YPaddingType:="	, "Absolute Offset",
                "-YPadding:="		, _fourth,
                "+ZPaddingType:="	, "Absolute Offset",
                "+ZPadding:="		, _fourth,
                "-ZPaddingType:="	, "Absolute Offset",
                "-ZPadding:="		, _fourth
            ],
            [
                "NAME:Attributes",
                "Name:="	, "Region",
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
            ]

        )

    def assign_radiation_region(self):
        self.oModule.AssignRadiation(
            [
                "NAME:Rad1",
                "Objects:="	, ["Region"],
                "IsFssReference:="	, False,
                "IsForPML:="		, False
            ])

    def assign_lumped(self, _obj, _start, _end):
        self.oModule.AssignLumpedPort(
            "NAME:1",
            "Objects:="	, _obj,
            "RenormalizeAllTerminals:=", True,
            "DoDeembed:="		, False,
            [
                "NAME:Modes",
                [
                    "NAME:Mode1",
                    "ModeNum:="		, 1,
                    "UseIntLine:="		, True,
                    [
                        "NAME:IntLine",
                        "Start:="		, _start,
                        "End:="			, _end
                    ],
                    "AlignmentGroup:="	, 0,
                    "CharImp:="		, "Zpi",
                    "RenormImp:="		, "50ohm"
                ]
            ],
            "ShowReporterFilter:="	, False,
            "ReporterFilter:="	, [True],
            "Impedance:="		, "50ohm"
        )

    def insert_setup(self, freq, max_passes):
        self.oModule.InsertSetup("HfssDriven",
                                 [
                                     "NAME:Setup1",
                                     "AdaptMultipleFreqs:=", False,
                                     "Frequency:="	, freq + "GHz",
                                     "MaxDeltaS:="		, 0.02,
                                     "PortsOnly:="		, False,
                                     "UseMatrixConv:="	, False,
                                     "MaximumPasses:="	, max_passes,
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

    def insert_sweep(self, range1, range2):
        self.oModule.InsertFrequencySweep(
            [
                "NAME:Sweep",
                "IsEnabled:="	, True,
                "RangeType:="		, "LinearCount",
                "RangeStart:="		, range1 + "GHz",
                "RangeEnd:="		, range2 + "GHz",
                "RangeCount:="		, 451,
                "Type:="		, "Fast",
                "SaveFields:="		, True,
                "SaveRadFields:="	, False,
                "GenerateFieldsForAllFreqs:=", False,
                "ExtrapToDC:="		, False
            ]
        )

    def insert_field_setup(self):
        mod = self.oDesign.GetModule("RadField")
        mod.InsertFarFieldSphereSetup(
            [
                "NAME:Infinite Sphere1",
                "UseCustomRadiationSurface:=", False,
                "ThetaStart:="	, "0deg",
                "ThetaStop:="		, "180deg",
                "ThetaStep:="		, "2deg",
                "PhiStart:="		, "0deg",
                "PhiStop:="		, "360deg",
                "PhiStep:="		, "2deg",
                "UseLocalCS:="		, False
            ])
        mod.InsertFarFieldSphereSetup(
            [
                "NAME:xy",
                "UseCustomRadiationSurface:=", False,
                "ThetaStart:="	, "90deg",
                "ThetaStop:="		, "90deg",
                "ThetaStep:="		, "2deg",
                "PhiStart:="		, "0deg",
                "PhiStop:="		, "360deg",
                "PhiStep:="		, "2deg",
                "UseLocalCS:="		, False
            ])
        mod.InsertFarFieldSphereSetup(
            [
                "NAME:xz",
                "UseCustomRadiationSurface:=", False,
                "ThetaStart:="	, "0deg",
                "ThetaStop:="		, "360deg",
                "ThetaStep:="		, "2deg",
                "PhiStart:="		, "0deg",
                "PhiStop:="		, "0deg",
                "PhiStep:="		, "2deg",
                "UseLocalCS:="		, False
            ])
        mod.InsertFarFieldSphereSetup(
            [
                "NAME:yz",
                "UseCustomRadiationSurface:=", False,
                "ThetaStart:="	, "0deg",
                "ThetaStop:="		, "360deg",
                "ThetaStep:="		, "2deg",
                "PhiStart:="		, "90deg",
                "PhiStop:="		, "90deg",
                "PhiStep:="		, "2deg",
                "UseLocalCS:="		, False
            ]
        )

    def create_report(self):
        mod = self.oDesign.GetModule("ReportSetup")
        mod.CreateReport(
            "S Parameter Plot 1", "Modal Solution Data", "Rectangular Plot", "Setup1 : Sweep",
            [
                "Domain:="	, "Sweep"
            ],
            [
                "Freq:="		, ["All"]
            ],
            [
                "X Component:="		, "Freq",
                "Y Component:="		, ["dB(S(1,1))"]
            ], []
        )
        mod.CreateReport(
            "Gain Plot 1", "Far Fields", "3D Polar Plot", "Setup1 : LastAdaptive",
            [
                "Context:="	, "Infinite Sphere1"
            ],
            [
                "Phi:="			, ["All"],
                "Theta:="		, ["All"],
                "Freq:="		, ["3GHz"]
            ],
            [
                "Phi Component:="	, "Phi",
                "Theta Component:="	, "Theta",
                "Mag Component:="	, ["dB(GainTotal)"]
            ], []
        )
        mod.CreateReport(
            "Gain Plot 2", "Far Fields", "Radiation Pattern", "Setup1 : LastAdaptive",
            [
                "Context:="	, "yz"
            ],
            [
                "Theta:="		, ["All"],
                "Phi:="			, ["All"],
                "Freq:="		, ["3GHz"]
            ],
            [
                "Ang Component:="	, "Theta",
                "Mag Component:="	, ["dB(GainTotal)"]
            ], []
        )
        mod.CreateReport(
            "Gain Plot 3", "Far Fields", "Radiation Pattern", "Setup1 : LastAdaptive",
            [
                "Context:="	, "xz"
            ],
            [
                "Theta:="		, ["All"],
                "Phi:="			, ["All"],
                "Freq:="		, ["3GHz"]
            ],
            [
                "Ang Component:="	, "Theta",
                "Mag Component:="	, ["dB(GainTotal)"]
            ], []
        )

    def save(self):
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
        self.oDesign.AnalyzeAll()
