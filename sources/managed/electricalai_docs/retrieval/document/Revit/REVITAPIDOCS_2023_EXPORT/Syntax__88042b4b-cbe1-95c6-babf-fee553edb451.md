[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SwitchPhases Method

---



|  |
| --- |
| [PanelScheduleView Class](ef4390e8-5a93-fe7f-580b-c8ec297f6b52.htm)   [See Also](#seeAlsoToggle) |

Switches the circuit phases at the slot.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public void SwitchPhases( 	int nRow, 	int nCol ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SwitchPhases ( _ 	nRow As Integer, _ 	nCol As Integer _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SwitchPhases( 	int nRow,  	int nCol ) ``` |

#### Parameters

nRow
:   Type:  System Int32    
     Row Number.

nCol
:   Type:  System Int32    
     Column Number.

# Remarks

Only one or two poles circuit on switchboard panel schedule can switch phases.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The circuit at given cell (nRow, nCol) is not one or two poles circuit. |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The given row number nRow is invalid in Body. -or- The given column number nCol is invalid in Body. -or- There is no circuit at given cell (nRow, nCol). |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This is not a switchboard panel schedule. |

# See Also

[PanelScheduleView Class](ef4390e8-5a93-fe7f-580b-c8ec297f6b52.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)