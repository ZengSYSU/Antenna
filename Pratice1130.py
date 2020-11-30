# -*- coding: utf-8 -*-

import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.NewProject()
oProject.InsertDesign("HFSS", "HFSSDesign1", "DrivenModal", "")
oDesign = oProject.SetActiveDesign("HFSSDesign1")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.SetModelUnits(
	[
		"NAME:Units Parameter",
		"Units:="		, "mm",
		"Rescale:="		, False
	])
oProject.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:ProjectVariableTab",
			[
				"NAME:PropServers",
				"ProjectVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:$w",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "16mm"
				],
				[
					"NAME:$l",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "32mm"
				],
				[
					"NAME:$h",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.8mm"
				],
				[
					"NAME:$wd",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "1.5mm"
				],
				[
					"NAME:$l1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "12mm"
				],
				[
					"NAME:$h1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "11mm"
				],
				[
					"NAME:$w1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "3mm"
				],
				[
					"NAME:$h2",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "20mm"
				],
				[
					"NAME:$h3",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "4mm"
				]
			]
		]
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-8mm",
		"YPosition:="		, "0mm",
		"ZPosition:="		, "0mm",
		"XSize:="		, "1mm",
		"YSize:="		, "1mm",
		"ZSize:="		, "1mm"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Box1",
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
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"Box1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "Substrate"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"Substrate"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Material",
					"Value:="		, "\"FR4_epoxy\""
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Substrate:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "-$w/2",
					"Y:="			, "0mm",
					"Z:="			, "0mm"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Substrate:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:XSize",
					"Value:="		, "$w"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Substrate:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:YSize",
					"Value:="		, "$l"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Substrate:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:ZSize",
					"Value:="		, "$h"
				]
			]
		]
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "0mm",
		"YStart:="		, "0mm",
		"ZStart:="		, "0mm",
		"Width:="		, "1mm",
		"Height:="		, "1mm",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle1",
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
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"Rectangle1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "microstrip"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"microstrip:CreateRectangle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "-$wd/2",
					"Y:="			, "0mm",
					"Z:="			, "$h"
				],
				[
					"NAME:XSize",
					"Value:="		, "$wd"
				],
				[
					"NAME:YSize",
					"Value:="		, "$l1"
				]
			]
		]
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "0mm",
		"YStart:="		, "0mm",
		"ZStart:="		, "0mm",
		"Width:="		, "1mm",
		"Height:="		, "1mm",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle1",
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
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"Rectangle1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "Groundplane"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Groundplane:CreateRectangle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:XSize",
					"Value:="		, "$w"
				],
				[
					"NAME:YSize",
					"Value:="		, "$h1"
				],
				[
					"NAME:Position",
					"X:="			, "-$w/2",
					"Y:="			, "0mm",
					"Z:="			, "0mm"
				]
			]
		]
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "0mm",
		"YStart:="		, "0mm",
		"ZStart:="		, "0mm",
		"Width:="		, "1mm",
		"Height:="		, "1mm",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle1",
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
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"Rectangle1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "patch"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"patch:CreateRectangle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "-$w/2",
					"Y:="			, "$l1",
					"Z:="			, "$h"
				],
				[
					"NAME:XSize",
					"Value:="		, "$w"
				],
				[
					"NAME:YSize",
					"Value:="		, "$h2"
				]
			]
		]
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "0mm",
		"YStart:="		, "0mm",
		"ZStart:="		, "0mm",
		"Width:="		, "1mm",
		"Height:="		, "1mm",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle1",
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
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"Rectangle1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "stair"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"stair:CreateRectangle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "-$w/2",
					"Y:="			, "$l1",
					"Z:="			, "$h"
				],
				[
					"NAME:XSize",
					"Value:="		, "$w1"
				],
				[
					"NAME:YSize",
					"Value:="		, "$h3"
				]
			]
		]
	])
oEditor.DuplicateMirror(
	[
		"NAME:Selections",
		"Selections:="		, "stair",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:DuplicateToMirrorParameters",
		"DuplicateMirrorBaseX:=", "0mm",
		"DuplicateMirrorBaseY:=", "12mm",
		"DuplicateMirrorBaseZ:=", "0.8mm",
		"DuplicateMirrorNormalX:=", "1mm",
		"DuplicateMirrorNormalY:=", "0mm",
		"DuplicateMirrorNormalZ:=", "0mm"
	], 
	[
		"NAME:Options",
		"DuplicateAssignments:=", False
	], 
	[
		"CreateGroupsForNewObjects:=", False
	])
oEditor.Subtract(
	[
		"NAME:Selections",
		"Blank Parts:="		, "patch",
		"Tool Parts:="		, "stair,stair_1"
	], 
	[
		"NAME:SubtractParameters",
		"KeepOriginals:="	, False
	])
oEditor.CreateRegion(
	[
		"NAME:RegionParameters",
		"+XPaddingType:="	, "Percentage Offset",
		"+XPadding:="		, "25",
		"-XPaddingType:="	, "Percentage Offset",
		"-XPadding:="		, "25",
		"+YPaddingType:="	, "Percentage Offset",
		"+YPadding:="		, "25",
		"-YPaddingType:="	, "Percentage Offset",
		"-YPadding:="		, "25",
		"+ZPaddingType:="	, "Percentage Offset",
		"+ZPadding:="		, "25",
		"-ZPaddingType:="	, "Percentage Offset",
		"-ZPadding:="		, "25"
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
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"Region"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "airbox"
				]
			]
		]
	])
oModule = oDesign.GetModule("BoundarySetup")
oModule.AssignRadiation(
	[
		"NAME:Rad1",
		"Objects:="		, ["airbox"],
		"IsFssReference:="	, False,
		"IsForPML:="		, False
	])
oModule.AssignPerfectE(
	[
		"NAME:PerfE1",
		"Objects:="		, ["patch","microstrip","Groundplane"],
		"InfGroundPlane:="	, False
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "0mm",
		"YStart:="		, "0mm",
		"ZStart:="		, "0mm",
		"Width:="		, "1mm",
		"Height:="		, "1mm",
		"WhichAxis:="		, "Y"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle1",
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
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"Rectangle1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "port"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"port:CreateRectangle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "-$wd/2",
					"Y:="			, "0mm",
					"Z:="			, "0mm"
				],
				[
					"NAME:XSize",
					"Value:="		, "$wd"
				],
				[
					"NAME:ZSize",
					"Value:="		, "$h"
				]
			]
		]
	])
oDesign.Undo()
oDesign.Redo()
oModule.AssignLumpedPort(
	[
		"NAME:1",
		"Objects:="		, ["port"],
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
					"Start:="		, ["0mm","7.4684943757722e-017mm","-1.37772764904077e-016mm"],
					"End:="			, ["1.11022302462516e-016mm","2.03334755731853e-016mm","0.8mm"]
				],
				"AlignmentGroup:="	, 0,
				"CharImp:="		, "Zpi",
				"RenormImp:="		, "50ohm"
			]
		],
		"ShowReporterFilter:="	, False,
		"ReporterFilter:="	, [True],
		"Impedance:="		, "50ohm"
	])
oModule = oDesign.GetModule("RadField")
oModule.InsertFarFieldSphereSetup(
	[
		"NAME:Infinite Sphere1",
		"UseCustomRadiationSurface:=", False,
		"ThetaStart:="		, "0deg",
		"ThetaStop:="		, "180deg",
		"ThetaStep:="		, "2deg",
		"PhiStart:="		, "0deg",
		"PhiStop:="		, "360deg",
		"PhiStep:="		, "2deg",
		"UseLocalCS:="		, False
	])
oModule.InsertFarFieldSphereSetup(
	[
		"NAME:XZ",
		"UseCustomRadiationSurface:=", False,
		"ThetaStart:="		, "0deg",
		"ThetaStop:="		, "360deg",
		"ThetaStep:="		, "2deg",
		"PhiStart:="		, "0deg",
		"PhiStop:="		, "0deg",
		"PhiStep:="		, "2deg",
		"UseLocalCS:="		, False
	])
oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:RadFieldSetupTab",
			[
				"NAME:PropServers", 
				"RadField:XZ"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Phi Step",
					"Value:="		, "0deg"
				]
			]
		]
	])
oModule.InsertFarFieldSphereSetup(
	[
		"NAME:ZY",
		"UseCustomRadiationSurface:=", False,
		"ThetaStart:="		, "0deg",
		"ThetaStop:="		, "360deg",
		"ThetaStep:="		, "2deg",
		"PhiStart:="		, "90deg",
		"PhiStop:="		, "90deg",
		"PhiStep:="		, "0deg",
		"UseLocalCS:="		, False
	])
oModule.InsertFarFieldSphereSetup(
	[
		"NAME:XY",
		"UseCustomRadiationSurface:=", False,
		"ThetaStart:="		, "90deg",
		"ThetaStop:="		, "90deg",
		"ThetaStep:="		, "0deg",
		"PhiStart:="		, "0deg",
		"PhiStop:="		, "360deg",
		"PhiStep:="		, "2deg",
		"UseLocalCS:="		, False
	])
oModule = oDesign.GetModule("AnalysisSetup")
oModule.InsertSetup("HfssDriven", 
	[
		"NAME:Setup1",
		"AdaptMultipleFreqs:="	, False,
		"Frequency:="		, "3GHz",
		"MaxDeltaS:="		, 0.02,
		"PortsOnly:="		, False,
		"UseMatrixConv:="	, False,
		"MaximumPasses:="	, 6,
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
oModule.InsertFrequencySweep("Setup1", 
	[
		"NAME:Sweep",
		"IsEnabled:="		, True,
		"RangeType:="		, "LinearCount",
		"RangeStart:="		, "2GHz",
		"RangeEnd:="		, "12GHz",
		"RangeCount:="		, 451,
		"Type:="		, "Fast",
		"SaveFields:="		, True,
		"SaveRadFields:="	, False,
		"GenerateFieldsForAllFreqs:=", False,
		"ExtrapToDC:="		, False
	])
oProject.SaveAs("C:\\Users\\tee\\Documents\\Ansoft\\pratice1130.aedt", True)
oDesign.AnalyzeAll()
oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("S Parameter Plot 1", "Modal Solution Data", "Rectangular Plot", "Setup1 : Sweep", 
	[
		"Domain:="		, "Sweep"
	], 
	[
		"Freq:="		, ["All"],
		"w:="			, ["Nominal"],
		"l:="			, ["Nominal"],
		"h:="			, ["Nominal"],
		"$w:="			, ["Nominal"],
		"$l:="			, ["Nominal"],
		"$h:="			, ["Nominal"],
		"$wd:="			, ["Nominal"],
		"$l1:="			, ["Nominal"],
		"$h1:="			, ["Nominal"],
		"$w1:="			, ["Nominal"],
		"$h2:="			, ["Nominal"],
		"$h3:="			, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["dB(S(1,1))"]
	], [])
oModule.CreateReport("Gain Plot 1", "Far Fields", "3D Polar Plot", "Setup1 : LastAdaptive", 
	[
		"Context:="		, "Infinite Sphere1"
	], 
	[
		"Phi:="			, ["All"],
		"Theta:="		, ["All"],
		"Freq:="		, ["3GHz"],
		"w:="			, ["Nominal"],
		"l:="			, ["Nominal"],
		"h:="			, ["Nominal"],
		"$w:="			, ["Nominal"],
		"$l:="			, ["Nominal"],
		"$h:="			, ["Nominal"],
		"$wd:="			, ["Nominal"],
		"$l1:="			, ["Nominal"],
		"$h1:="			, ["Nominal"],
		"$w1:="			, ["Nominal"],
		"$h2:="			, ["Nominal"],
		"$h3:="			, ["Nominal"]
	], 
	[
		"Phi Component:="	, "Phi",
		"Theta Component:="	, "Theta",
		"Mag Component:="	, ["dB(GainTotal)"]
	], [])
oModule.CreateReport("Gain Plot 2", "Far Fields", "Radiation Pattern", "Setup1 : LastAdaptive", 
	[
		"Context:="		, "ZY"
	], 
	[
		"Theta:="		, ["All"],
		"Phi:="			, ["All"],
		"Freq:="		, ["3GHz"],
		"w:="			, ["Nominal"],
		"l:="			, ["Nominal"],
		"h:="			, ["Nominal"],
		"$w:="			, ["Nominal"],
		"$l:="			, ["Nominal"],
		"$h:="			, ["Nominal"],
		"$wd:="			, ["Nominal"],
		"$l1:="			, ["Nominal"],
		"$h1:="			, ["Nominal"],
		"$w1:="			, ["Nominal"],
		"$h2:="			, ["Nominal"],
		"$h3:="			, ["Nominal"]
	], 
	[
		"Ang Component:="	, "Theta",
		"Mag Component:="	, ["dB(GainTotal)"]
	], [])
oModule.CreateReport("Gain Plot 3", "Far Fields", "Radiation Pattern", "Setup1 : LastAdaptive", 
	[
		"Context:="		, "XZ"
	], 
	[
		"Theta:="		, ["All"],
		"Phi:="			, ["All"],
		"Freq:="		, ["3GHz"],
		"w:="			, ["Nominal"],
		"l:="			, ["Nominal"],
		"h:="			, ["Nominal"],
		"$w:="			, ["Nominal"],
		"$l:="			, ["Nominal"],
		"$h:="			, ["Nominal"],
		"$wd:="			, ["Nominal"],
		"$l1:="			, ["Nominal"],
		"$h1:="			, ["Nominal"],
		"$w1:="			, ["Nominal"],
		"$h2:="			, ["Nominal"],
		"$h3:="			, ["Nominal"]
	], 
	[
		"Ang Component:="	, "Theta",
		"Mag Component:="	, ["dB(GainTotal)"]
	], [])
oModule = oDesign.GetModule("Optimetrics")
oModule.InsertSetup("OptiParametric", 
	[
		"NAME:ParametricSetup1",
		"IsEnabled:="		, True,
		[
			"NAME:ProdOptiSetupDataV2",
			"SaveFields:="		, False,
			"CopyMesh:="		, False,
			"SolveWithCopiedMeshOnly:=", True
		],
		[
			"NAME:StartingPoint"
		],
		"Sim. Setups:="		, ["Setup1"],
		[
			"NAME:Sweeps",
			[
				"NAME:SweepDefinition",
				"Variable:="		, "$w1",
				"Data:="		, "LIN 3mm 5mm 0.5mm",
				"OffsetF1:="		, False,
				"Synchronize:="		, 0
			]
		],
		[
			"NAME:Sweep Operations"
		],
		[
			"NAME:Goals"
		]
	])
oProject.Save()
oDesign.AnalyzeAll()
oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("S Parameter Plot 2", "Modal Solution Data", "Rectangular Plot", "Setup1 : Sweep", 
	[
		"Domain:="		, "Sweep"
	], 
	[
		"Freq:="		, ["All"],
		"w:="			, ["Nominal"],
		"l:="			, ["Nominal"],
		"h:="			, ["Nominal"],
		"$w:="			, ["Nominal"],
		"$l:="			, ["Nominal"],
		"$h:="			, ["Nominal"],
		"$wd:="			, ["Nominal"],
		"$l1:="			, ["Nominal"],
		"$h1:="			, ["Nominal"],
		"$w1:="			, ["All"],
		"$h2:="			, ["Nominal"],
		"$h3:="			, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["dB(S(1,1))"]
	], [])

