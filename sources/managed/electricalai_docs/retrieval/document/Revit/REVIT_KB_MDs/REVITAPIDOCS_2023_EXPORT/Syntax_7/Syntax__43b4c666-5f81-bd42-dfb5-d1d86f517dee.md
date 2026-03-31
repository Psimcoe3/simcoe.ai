[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StructuralWallUsageFilter Class

---



|  |
| --- |
| [Members](de860e18-edea-1d67-68e6-159f8db23a95.htm)   [See Also](#seeAlsoToggle) |

A filter used to match walls that have the given structural wall usage.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public class StructuralWallUsageFilter : ElementSlowFilter ``` |

 

| Visual Basic |
| --- |
| ``` Public Class StructuralWallUsageFilter _ 	Inherits ElementSlowFilter ``` |

 

| Visual C++ |
| --- |
| ``` public ref class StructuralWallUsageFilter : public ElementSlowFilter ``` |

# Remarks

This filter is a slow filter, but it uses a quick filter to eliminate non-candidate elements before the elements are obtained and expanded. Therefore this filter does not have to be paired with another quick filter to minimize the number of Elements that are expanded.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)    
  [Autodesk.Revit.DB ElementSlowFilter](e06b1e14-dd8d-8137-74ac-8ac4929eee85.htm)    
  Autodesk.Revit.DB.Structure StructuralWallUsageFilter

# See Also

[StructuralWallUsageFilter Members](de860e18-edea-1d67-68e6-159f8db23a95.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)