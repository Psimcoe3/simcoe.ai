[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarInSystem Class

---



|  |
| --- |
| [Members](79d20775-2df3-a041-3226-b63ecbb8ec2f.htm)   [See Also](#seeAlsoToggle) |

Represents a rebar element that is part of a system.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public class RebarInSystem : Element ``` |

 

| Visual Basic |
| --- |
| ``` Public Class RebarInSystem _ 	Inherits Element ``` |

 

| Visual C++ |
| --- |
| ``` public ref class RebarInSystem : public Element ``` |

# Remarks

A RebarInSystem element is part of another element, the "system", which controls most of its properties. The system elements are AreaReinforcement and PathReinforcement. Only a few properties of RebarInSystem are modifiable. Otherwise, the appearance and behavior of RebarInSystem elements is identical to Rebar elements. RebarInSystem elements may be converted to Rebar elements by removing the system element.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  Autodesk.Revit.DB.Structure RebarInSystem

# See Also

[RebarInSystem Members](79d20775-2df3-a041-3226-b63ecbb8ec2f.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)