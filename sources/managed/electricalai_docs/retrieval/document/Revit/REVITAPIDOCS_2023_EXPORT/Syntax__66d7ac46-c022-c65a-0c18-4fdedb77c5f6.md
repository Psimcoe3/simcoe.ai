[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetRebarInSystemIds Method

---



|  |
| --- |
| [PathReinforcement Class](1593a849-b883-73d4-7c02-a2522877d71d.htm)   [See Also](#seeAlsoToggle) |

Returns the ids of the RebarInSystem elements owned by the PathReinforcement element.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public IList<ElementId> GetRebarInSystemIds() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetRebarInSystemIds As IList(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<ElementId^>^ GetRebarInSystemIds() ``` |

# Remarks

The RebarInSystem elements are only created if ReinforcementSettings.HostStructuralRebar is set to true. If that setting is false, this function returns an empty array.

# See Also

[PathReinforcement Class](1593a849-b883-73d4-7c02-a2522877d71d.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)