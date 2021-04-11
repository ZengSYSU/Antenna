# -*- coding: utf-8 -*-
from win32com import client


def Prj(_phase1, _phase2, _phase3, _phase4, _phase5, _phase6, _phase7, _phase8):
    oAnsoftApp = client.Dispatch('AnsoftHfss.HfssScriptInterface')
    oDesktop = oAnsoftApp.GetAppDesktop()
    oDesktop.OpenProject("C:/Users/tee/PycharmProjects/Prj4.aedt")
    oProject = oDesktop.SetActiveProject("Prj4")
    oDesign = oProject.SetActiveDesign("HFSSDesign1")
    oModule = oDesign.GetModule("Solutions")
    oModule.EditSources(
        [
                [
                    "IncludePortPostProcessing:=", True,
                    "SpecifySystemPower:=", False
                ],
                [
                    "Name:=", "lumpedPort1:1",
                    "Magnitude:=", '1W',
                    "Phase:="	, str(_phase1) + "deg"
                    ],
                [
                        "Name:="		, "lumpedPort2:1",
                        "Magnitude:="	, '1W',
                        "Phase:="		, str(_phase2) + "deg"
                    ],
                [
                        "Name:="		, "lumpedPort3:1",
                        "Magnitude:="	, '1W',
                        "Phase:="		, str(_phase3) + "deg"
                    ],
                [
                        "Name:="		, "lumpedPort4:1",
                        "Magnitude:="	, '1W',
                        "Phase:="		, str(_phase4) + "deg"
                    ],
                [
                        "Name:="		, "lumpedPort5:1",
                        "Magnitude:="	, '1W',
                        "Phase:="		, str(_phase5) + "deg"
                    ],
                [
                        "Name:="		, "lumpedPort6:1",
                        "Magnitude:="	,  '1W',
                        "Phase:="		, str(_phase6) + "deg"
                    ],
                [
                        "Name:="		, "lumpedPort7:1",
                        "Magnitude:="	, '1W',
                        "Phase:="		, str(_phase7) + "deg"
                    ],
                [
                        "Name:="		, "lumpedPort8:1",
                        "Magnitude:="	, '1W',
                        "Phase:="		, str(_phase8) + "deg"
                    ]
            ])
    oModule = oDesign.GetModule("ReportSetup")
    oModule.ExportToFile("Gain Plot 2", "C:/Users/tee/PycharmProjects/Gain Plot 2.csv")
    oProject.save()
    oDesktop.CloseProject("Prj4")


if __name__ == '__main__':
    Prj(0, 0, 0, 0, 0, 0, 0, 0)
