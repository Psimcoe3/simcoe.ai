[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetOffsetForLocationLine Method

---



|  |
| --- |
| [CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.htm)   [See Also](#seeAlsoToggle) |

Returns the offset from the center of the compound structure to the given location line value.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public double GetOffsetForLocationLine( 	WallLocationLine wallLocationLine ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetOffsetForLocationLine ( _ 	wallLocationLine As WallLocationLine _ ) As Double ``` |

 

| Visual C++ |
| --- |
| ``` public: double GetOffsetForLocationLine( 	WallLocationLine wallLocationLine ) ``` |

#### Parameters

wallLocationLine
:   Type:  [Autodesk.Revit.DB WallLocationLine](87090d88-570b-6f84-cf87-63414b51ece0.htm)    
     The alignment type of the wall's location line.

#### Return Value

The offset.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This operation is valid only vertically homogeneous compound structures. |

# See Also

[CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)