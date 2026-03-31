[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StructuralMaterialTypeFilter Class

---



|  |
| --- |
| [Members](499d9bfc-6cca-b995-942f-ac413e7e66dc.htm)   [See Also](#seeAlsoToggle) |

A filter used to match family instances that have the given structural material type.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public class StructuralMaterialTypeFilter : ElementSlowFilter ``` |

 

| Visual Basic |
| --- |
| ``` Public Class StructuralMaterialTypeFilter _ 	Inherits ElementSlowFilter ``` |

 

| Visual C++ |
| --- |
| ``` public ref class StructuralMaterialTypeFilter : public ElementSlowFilter ``` |

# Remarks

This filter is a slow filter, but it uses a quick filter to eliminate non-candidate elements before the elements are obtained and expanded. Therefore this filter does not have to be paired with another quick filter to minimize the number of Elements that are expanded.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)    
  [Autodesk.Revit.DB ElementSlowFilter](e06b1e14-dd8d-8137-74ac-8ac4929eee85.htm)    
  Autodesk.Revit.DB.Structure StructuralMaterialTypeFilter

# See Also

[StructuralMaterialTypeFilter Members](499d9bfc-6cca-b995-942f-ac413e7e66dc.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)