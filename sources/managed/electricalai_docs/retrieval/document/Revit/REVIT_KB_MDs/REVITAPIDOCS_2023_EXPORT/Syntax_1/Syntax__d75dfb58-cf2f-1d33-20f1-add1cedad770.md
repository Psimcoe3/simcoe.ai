[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StructuralInstanceUsageFilter Class

---



|  |
| --- |
| [Members](aa5e4d8b-97b7-7a23-864e-f5d3a06bd551.htm)   [See Also](#seeAlsoToggle) |

A filter used to find elements that are structural family instances (typically columns, beams or braces) of the given structural usage.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public class StructuralInstanceUsageFilter : ElementSlowFilter ``` |

 

| Visual Basic |
| --- |
| ``` Public Class StructuralInstanceUsageFilter _ 	Inherits ElementSlowFilter ``` |

 

| Visual C++ |
| --- |
| ``` public ref class StructuralInstanceUsageFilter : public ElementSlowFilter ``` |

# Remarks

This filter is a slow filter, but it uses a quick filter to eliminate non-candidate elements before the elements are obtained and expanded. Therefore this filter does not have to be paired with another quick filter to minimize the number of Elements that are expanded.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)    
  [Autodesk.Revit.DB ElementSlowFilter](e06b1e14-dd8d-8137-74ac-8ac4929eee85.htm)    
  Autodesk.Revit.DB.Structure StructuralInstanceUsageFilter

# See Also

[StructuralInstanceUsageFilter Members](aa5e4d8b-97b7-7a23-864e-f5d3a06bd551.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)