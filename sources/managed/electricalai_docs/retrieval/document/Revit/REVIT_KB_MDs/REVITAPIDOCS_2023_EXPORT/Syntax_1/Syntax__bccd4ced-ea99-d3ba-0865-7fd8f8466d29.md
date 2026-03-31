[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetLayerDirection Method

---



|  |
| --- |
| [AreaReinforcement Class](889aa3cf-9b32-dd78-b660-bcfbad2cf87e.htm)   [See Also](#seeAlsoToggle) |

Gets the direction of the layer. The lines are distributed along this direction.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public XYZ GetLayerDirection( 	AreaReinforcementLayerType layer ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetLayerDirection ( _ 	layer As AreaReinforcementLayerType _ ) As XYZ ``` |

 

| Visual C++ |
| --- |
| ``` public: XYZ^ GetLayerDirection( 	AreaReinforcementLayerType layer ) ``` |

#### Parameters

layer
:   Type:  [Autodesk.Revit.DB.Structure AreaReinforcementLayerType](46b15eb7-46c4-2ed9-df2d-417777518f18.htm)    
     The layer type.

#### Return Value

Returns the direction of the desired layer.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions InapplicableDataException](dc1a6d15-8923-a1fe-722a-4e976634a519.htm) | The layer layer isn't active. |

# See Also

[AreaReinforcement Class](889aa3cf-9b32-dd78-b660-bcfbad2cf87e.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)