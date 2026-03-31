[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsSlotLocked Method

---



|  |
| --- |
| [PanelScheduleView Class](ef4390e8-5a93-fe7f-580b-c8ec297f6b52.htm)   [See Also](#seeAlsoToggle) |

Check if the circuit slot in this cell is locked.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)

# Syntax

| C# |
| --- |
| ``` public bool IsSlotLocked( 	int nRow, 	int nCol ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsSlotLocked ( _ 	nRow As Integer, _ 	nCol As Integer _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsSlotLocked( 	int nRow,  	int nCol ) ``` |

#### Parameters

nRow
:   Type:  System Int32    
     Row Number

nCol
:   Type:  System Int32    
     Column Number

#### Return Value

True if the circuit slot in this cell is locked, false otherwise False if the circuit slot not found.

# See Also

[PanelScheduleView Class](ef4390e8-5a93-fe7f-580b-c8ec297f6b52.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)