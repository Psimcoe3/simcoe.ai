[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AreCoordinatesInBounds Method

---



|  |
| --- |
| [RepeaterBounds Class](99c1ffdf-818b-1918-a6ba-42b7904ca4bc.htm)   [See Also](#seeAlsoToggle) |

Determines whether given coordinates are within the bounds.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public bool AreCoordinatesInBounds( 	RepeaterCoordinates coordinates, 	bool treatCyclicalBoundsAsInfinite ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function AreCoordinatesInBounds ( _ 	coordinates As RepeaterCoordinates, _ 	treatCyclicalBoundsAsInfinite As Boolean _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool AreCoordinatesInBounds( 	RepeaterCoordinates^ coordinates,  	bool treatCyclicalBoundsAsInfinite ) ``` |

#### Parameters

coordinates
:   Type:  [Autodesk.Revit.DB RepeaterCoordinates](17102857-7a63-7039-f5f4-88d07dc33c7a.htm)    
     The coordinates.

treatCyclicalBoundsAsInfinite
:   Type:  System Boolean    
     True if cyclical directions should be treated as unbounded.

#### Return Value

True if the coordinates are within the bounds.

# Remarks

The coordinates must have the same number of dimensions as the bounds. This method does not apply to zero dimensional bounds.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The coordinates coordinates have incompatible number of dimensions. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The bounds must have at least one dimension. |

# See Also

[RepeaterBounds Class](99c1ffdf-818b-1918-a6ba-42b7904ca4bc.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)