[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetRebarInSystemIds Method

---



|  |
| --- |
| [AreaReinforcement Class](889aa3cf-9b32-dd78-b660-bcfbad2cf87e.htm)   [See Also](#seeAlsoToggle) |

Returns the ids of the RebarInSystem elements owned by the AreaReinforcement element.

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

[AreaReinforcement Class](889aa3cf-9b32-dd78-b660-bcfbad2cf87e.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)