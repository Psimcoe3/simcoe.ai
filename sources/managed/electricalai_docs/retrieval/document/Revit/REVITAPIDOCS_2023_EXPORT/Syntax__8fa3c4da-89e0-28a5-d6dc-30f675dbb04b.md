[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetLineFromLayerAtIndex Method

---



|  |
| --- |
| [AreaReinforcement Class](889aa3cf-9b32-dd78-b660-bcfbad2cf87e.htm)   [See Also](#seeAlsoToggle) |

Gets the line from the desired layer at the specified index.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public Line GetLineFromLayerAtIndex( 	AreaReinforcementLayerType layer, 	int linePositionIndex ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetLineFromLayerAtIndex ( _ 	layer As AreaReinforcementLayerType, _ 	linePositionIndex As Integer _ ) As Line ``` |

 

| Visual C++ |
| --- |
| ``` public: Line^ GetLineFromLayerAtIndex( 	AreaReinforcementLayerType layer,  	int linePositionIndex ) ``` |

#### Parameters

layer
:   Type:  [Autodesk.Revit.DB.Structure AreaReinforcementLayerType](46b15eb7-46c4-2ed9-df2d-417777518f18.htm)    
     The layer on which the line stays.

linePositionIndex
:   Type:  System Int32    
     The index of the line from the desired layer. It should be an index between 0 and (NumberOfLines-1).

#### Return Value

Returns the line from the desired layer at the specified index.

# Remarks

This method will return the line even if it isn't included.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | linePositionIndex is not in the range [ 0, NumberOfLines-1 ]. -or- A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions InapplicableDataException](dc1a6d15-8923-a1fe-722a-4e976634a519.htm) | The layer layer isn't active. |

# See Also

[AreaReinforcement Class](889aa3cf-9b32-dd78-b660-bcfbad2cf87e.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)