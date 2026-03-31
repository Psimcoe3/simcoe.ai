[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetCoordinate Method

---



|  |
| --- |
| [RepeaterCoordinates Class](17102857-7a63-7039-f5f4-88d07dc33c7a.htm)   [See Also](#seeAlsoToggle) |

Returns the coordinate in the given dimension.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public int GetCoordinate( 	int dimension ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetCoordinate ( _ 	dimension As Integer _ ) As Integer ``` |

 

| Visual C++ |
| --- |
| ``` public: int GetCoordinate( 	int dimension ) ``` |

#### Parameters

dimension
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The dimension.

#### Return Value

The coordinate.

# Remarks

The dimension begins at 0 and must be in the range [0, number of dimensions in the bounds - 1]. This method does not apply to zero dimensional coordinates.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The dimension is invalid for these coordinates. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The coordinates must have at least one dimension. |

# See Also

[RepeaterCoordinates Class](17102857-7a63-7039-f5f4-88d07dc33c7a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)