[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ClearWallSweeps Method

---



|  |
| --- |
| [CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.htm)   [See Also](#seeAlsoToggle) |

Removes all sweeps or reveals from the compound structure.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public void ClearWallSweeps( 	WallSweepType wallSweepType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub ClearWallSweeps ( _ 	wallSweepType As WallSweepType _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void ClearWallSweeps( 	WallSweepType wallSweepType ) ``` |

#### Parameters

wallSweepType
:   Type:  [Autodesk.Revit.DB WallSweepType](f66354e5-a9c6-de97-695c-4a2fba036232.htm)    
     The type of a wall sweep.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This operation is valid only for vertically compound structures. |

# See Also

[CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)