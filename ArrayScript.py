# -*- coding: utf-8 -*-
from win32com import client
import os


class HFSS:
    def __init__(self):
        self.oAnsoftApp = client.Dispatch('AnsoftHfss.HfssScriptInterface')
        self.oDesktop = self.oAnsoftApp.GetDesktop()
        self.oProject = self.oDesktop.NewProject()
        self.oProject.InsertDesign('HFSS', 'HFSSDesign1', 'DrivenModal1', '')
        self.oDesign = self.oProject.SetActiveDesign('HFSSDesign1')
        self.oEditor = self.oDesign.SetActiveEditor("3D Modeler")
        self.oModule = self.oDesign.GetModule('BoundarySetup')

    def set_var(self, _var_name, _var_value):
        _NAME = 'NAME:' + _var_name
        _VALUE = str(_var_value) + 'in'
        self.oDesign.ChangeProperty(
            [
                "NAME:ALLTabs",
                [
                    "NAME:ProjectVariableTab",
                    [
                        "NAME:ProServers", "ProjectVariableTab"
                    ],
                    [
                        "NAME:NewProps",
                        [
                            _NAME, "ProType:=", "VariableProp", "UserDef:=", True, "Value:=", _VALUE
                        ]
                    ]
                ]
            ]
        )

    def create_box(self, _var_x, _var_y, _var_z, _var_dx, _var_dy, _var_dz, _name):
        self.oEditor.CreateBox(
            [
                "NAME:BoxParameters",
                "XPosition:=", _var_x,
                "YPosition:=", _var_y,
                "ZPosition:=", _var_z,
                "XSize:=",     _var_dx,
                "YSize:=",     _var_dy,
                "ZSize:=",     _var_dz,
            ],
            [
                "NAME:Attributes",
                "Name:=", _name,
                "Flags:=", "",
                "Color:=", "(143 175 143)",
                "Transparency:=", 0.5,
                "PartCoordinateSystem:=", "Global",
                "UDMId:=", "",
                "MaterialValue:=", "\"vacuum\"",
                "SurfaceMaterialValue:=", "\"\"",
                "SolveInside:="	, True,
                "IsMaterialEditable:="	, True,
                "UseMaterialAppearance:=", False
            ]
        )

    def assign_master(self):
        mod = self.oDesign.GetModule("BoundarySetup")
        mod.AssignMaster(
            [
                "NAME:Master1",
                "Faces:="	, [40],
                [
                    "NAME:CoordSysVector",
                    "Origin:="		, ["0.45in", "-0.05in", "1in"],
                    "UPos:="		, ["0.45in", "0.95in", "1in"]
                ],
                "ReverseV:="		, True
            ]
        )
        mod.AssignMaster(
            [
                "NAME:Master2",
                "Faces:=", [39],
                [
                    "NAME:CoordSysVector",
                    "Origin:="	,     ["0.45in", "0.95in", "1in"],
                    "UPos:="		, ["-0.05in", "0.95in", "1in"]
                ],
                "ReverseV:="		, True
            ]
        )

    def assign_slave(self, _phi, _theta):
        mod = self.oDesign.GetModule("BoundarySetup")
        mod.AssignSlave(
            [
                "NAME:Slave1",
                "Faces:="	, [38],
                [
                    "NAME:CoordSysVector",
                    "Origin:="		, ["-0.05in", "-0.05in", "1in"],
                    "UPos:="		, ["-0.05in", "0.95in", "1in"]
                ],
                "ReverseV:="		, False,
                "Master:="		, "Master1",
                "UseScanAngles:="	, True,
                "Phi:="			, str(_phi) + 'deg',
                "Theta:="		, str(_theta) + 'deg'
            ])
        mod.AssignSlave(
            [
                "NAME:Slave2",
                "Faces:=", [37],
                [
                    "NAME:CoordSysVector",
                    "Origin:="	,     ["0.45in", "-0.05in", "1in"],
                    "UPos:="		, ["-0.05in", "-0.05in", "1in"]
                ],
                "ReverseV:="		, False,
                "Master:="		, "Master2",
                "UseScanAngles:="	, True,
                "Phi:="			, str(_phi) + 'deg',
                "Theta:="		, str(_theta) + 'deg'
            ]
        )

    def assign_fp(self):
        self.oModule.AssignFloquetPort(
            [
                "NAME:FloquetPort1",
                "Faces:="	, [35],
                "NumModes:="		, 4,
                "RenormalizeAllTerminals:=", True,
                "DoDeembed:="		, False,
                [
                    "NAME:Modes",
                    ["NAME:Mode1", "ModeNum:=", 1, "UseIntLine:=", False, "CharImp:=", "Zpi"],
                    ["NAME:Mode2", "ModeNum:=", 2, "UseIntLine:=", False, "CharImp:=", "Zpi"],
                    ["NAME:Mode3", "ModeNum:=", 3, "UseIntLine:=", False, "CharImp:=", "Zpi"],
                    ["NAME:Mode4", "ModeNum:=", 4, "UseIntLine:=", False, "CharImp:=", "Zpi"]
                ],
                "ShowReporterFilter:="	, False,
                "ReporterFilter:="	, [False, False, False, False],
                "UseScanAngles:="	, True,
                "Phi:="			, "0deg",
                "Theta:="		, "30deg",
                [
                    "NAME:LatticeAVector",
                    "Start:="		, ["0.45in", "-0.05in", "2in"],
                    "End:="			, ["0.45in", "0.95in", "2in"]
                ],
                [
                    "NAME:LatticeBVector",
                    "Start:="		, ["0.45in", "-0.05in", "2in"],
                    "End:="			, ["-0.05in", "-0.05in", "2in"]
                ],
                [
                    "NAME:ModesCalculator",
                    "Frequency:="		, "9.25GHz",
                    "FrequencyChanged:="	, True,
                    "PhiStart:="		, "0deg",
                    "PhiStop:="		, "90deg",
                    "PhiStep:="		, "10deg",
                    "ThetaStart:="		, "0deg",
                    "ThetaStop:="		, "90deg",
                    "ThetaStep:="		, "10deg"
                ],
                [
                    "NAME:ModesList",
                    [
                        "NAME:Mode",
                        "ModeNumber:="		, 1,
                        "IndexM:="		, 0,
                        "IndexN:="		, 0,
                        "KC2:="			, 0,
                        "PropagationState:="	, "Propagating",
                        "Attenuation:="		, 0,
                        "PolarizationState:="	, "TE",
                        "AffectsRefinement:="	, True
                    ],
                    [
                        "NAME:Mode",
                        "ModeNumber:="		, 2,
                        "IndexM:="		, 0,
                        "IndexN:="		, 0,
                        "KC2:="			, 0,
                        "PropagationState:="	, "Propagating",
                        "Attenuation:="		, 0,
                        "PolarizationState:="	, "TM",
                        "AffectsRefinement:="	, True
                    ],
                    [
                        "NAME:Mode",
                        "ModeNumber:="		, 3,
                        "IndexM:="		, -1,
                        "IndexN:="		, 0,
                        "KC2:="			, 0,
                        "PropagationState:="	, "Propagating",
                        "Attenuation:="		, 0,
                        "PolarizationState:="	, "TE",
                        "AffectsRefinement:="	, True
                    ],
                    [
                        "NAME:Mode",
                        "ModeNumber:="		, 4,
                        "IndexM:="		, -1,
                        "IndexN:="		, 0,
                        "KC2:="			, 0,
                        "PropagationState:="	, "Propagating",
                        "Attenuation:="		, 0,
                        "PolarizationState:="	, "TM",
                        "AffectsRefinement:="	, True
                    ]
                ]
            ]
        )

    def assign_wave_port(self):
        self.oModule.AssignWavePort(
            [
                "NAME:1",
                "Faces:="	, [8],
                "NumModes:="		, 1,
                "RenormalizeAllTerminals:=", True,
                "UseLineModeAlignment:=", False,
                "DoDeembed:="		, False,
                [
                    "NAME:Modes",
                    [
                        "NAME:Mode1",
                        "ModeNum:="		, 1,
                        "UseIntLine:="		, False,
                        "CharImp:="		, "Zpi"
                    ]
                ],
                "ShowReporterFilter:="	, False,
                "ReporterFilter:="	, [True],
                "UseAnalyticAlignment:=", False
            ]
        )

    def insert_setup(self, _freq):
        mod = self.oDesign.GetModule('AnalysisSetup')
        mod.InsertSetup("HfssDriven",
                        [
                            "NAME:Setup1",
                            "AdaptMultipleFreqs:=", False,
                            "Frequency:="	, str(_freq) + 'GHz',
                            "MaxDeltaS:="		, 0.02,
                            "PortsOnly:="		, False,
                            "UseMatrixConv:="	, False,
                            "MaximumPasses:="	, 10,
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

    def insert_field_setup(self):
        mod = self.oDesign.GetModule("RadField")
        mod.InsertFarFieldSphereSetup(
            [
                "NAME:Infinite Sphere1",
                "UseCustomRadiationSurface:=", False,
                "ThetaStart:="	, "0deg",
                "ThetaStop:="		, "180deg",
                "ThetaStep:="		, "10deg",
                "PhiStart:="		, "-180deg",
                "PhiStop:="		, "180deg",
                "PhiStep:="		, "10deg",
                "UseLocalCS:="		, False
            ])
        mod.InsertFarFieldSphereSetup(
            [
                "NAME:Infinite Sphere2",
                "UseCustomRadiationSurface:=", False,
                "ThetaStart:="	, "0deg",
                "ThetaStop:="		, "360deg",
                "ThetaStep:="		, "10deg",
                "PhiStart:="		, "0deg",
                "PhiStop:="		, "90deg",
                "PhiStep:="		, "90deg",
                "UseLocalCS:="		, False
            ])

    def create_report(self):
        mod = self.oDesign.GetModule("ReportSetup")
        mod.CreateReport(
            "rE Plot 1", "Far Fields", "Radiation Pattern", "Setup1 : LastAdaptive",
            [
                "Context:="	, "Infinite Sphere2"
            ],
            [
                "Theta:="		, ["All"],
                "Phi:="			, ["All"],
                "Freq:="		, ["All"]
            ],
            [
                "Ang Component:="	, "Theta",
                "Mag Component:="	, ["dB(rETotal)"]
            ], []
        )
        mod.CreateReport(
            "rE Plot 2", "Far Fields", "3D Polar Plot", "Setup1 : LastAdaptive",
            [
                "Context:="	, "Infinite Sphere1"
            ],
            [
                "Phi:="			, ["All"],
                "Theta:="		, ["All"],
                "Freq:="		, ["All"]
            ],
            [
                "Phi Component:="	, "Phi",
                "Theta Component:="	, "Theta",
                "Mag Component:="	, ["dB(rETotal)"]
            ], []
        )

    def array(self, _u, _v, _ud, _vd):
        mod = self.oDesign.GetModule("RadField")
        mod.EditAntennaArraySetup(
            [
                "NAME:ArraySetupInfo",
                "UseOption:="	, "RegularArray",
                [
                    "NAME:RegularArray",
                    "NumUCells:="		, _u,
                    "NumVCells:="		, _v,
                    "CellUDist:="		, _ud,
                    "CellVDist:="		, _vd,
                    "UDirnX:="		, "1",
                    "UDirnY:="		, "0",
                    "UDirnZ:="		, "0",
                    "VDirnX:="		, "0",
                    "VDirnY:="		, "1",
                    "VDirnZ:="		, "0",
                    "FirstCellPosX:="	, "0mm",
                    "FirstCellPosY:="	, "0mm",
                    "FirstCellPosZ:="	, "0mm",
                    "Behavior:="		, "UseSlaveSettings"
                ],
                [
                    "NAME:CustomArray",
                    "NumCells:="		, 0,
                    [
                        "NAME:Cell"
                    ]
                ]
            ]
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
