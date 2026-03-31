[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MoveSlotTo Method

---



|  |
| --- |
| [PanelScheduleView Class](ef4390e8-5a93-fe7f-580b-c8ec297f6b52.htm)   [See Also](#seeAlsoToggle) |

Move the circuits in the source slot to the specific slot.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)

# Syntax

| C# |
| --- |
| ``` public void MoveSlotTo( 	int nMovingRow, 	int nMovingCol, 	int nToRow, 	int nToCol ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub MoveSlotTo ( _ 	nMovingRow As Integer, _ 	nMovingCol As Integer, _ 	nToRow As Integer, _ 	nToCol As Integer _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void MoveSlotTo( 	int nMovingRow,  	int nMovingCol,  	int nToRow,  	int nToCol ) ``` |

#### Parameters

nMovingRow
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The Row Number of cell to be moved.

nMovingCol
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     Start Column Number of cell to be moved.

nToRow
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The Row Number of cell to moved to.

nToCol
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     End Column Number of cell to moved to.

# Remarks

If the moving circuit is in a group, all circuits in the group will be moved accordingly.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The given row number nMovingRow is invalid in Body. -or- The given column number nMovingCol is invalid in Body. -or- The given row number nToRow is invalid in Body. -or- The given column number nToCol is invalid in Body. -or- There is no circuit at given cell (nMovingRow, nMovingCol). -or- Cannot move the circuits at slot (nMovingRow, nMovingCol) to given slot (nToRow, nToCol). |

# See Also

[PanelScheduleView Class](ef4390e8-5a93-fe7f-580b-c8ec297f6b52.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)