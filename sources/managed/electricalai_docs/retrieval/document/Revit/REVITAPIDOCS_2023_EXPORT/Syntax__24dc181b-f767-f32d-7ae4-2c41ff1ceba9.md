[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RoomTagFilter Class

---



|  |
| --- |
| [Members](c8b0c293-bb69-c045-0ce4-704fb54da5a1.htm)   [See Also](#seeAlsoToggle) |

A filter used to match room tags.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class RoomTagFilter : ElementSlowFilter ``` |

 

| Visual Basic |
| --- |
| ``` Public Class RoomTagFilter _ 	Inherits ElementSlowFilter ``` |

 

| Visual C++ |
| --- |
| ``` public ref class RoomTagFilter : public ElementSlowFilter ``` |

# Remarks

This filter is a slow filter, but it uses a quick filter to eliminate non-candidate elements before the elements are obtained and expanded. Therefore this filter does not have to be paired with another quick filter to minimize the number of Elements that are expanded.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)    
  [Autodesk.Revit.DB ElementSlowFilter](e06b1e14-dd8d-8137-74ac-8ac4929eee85.htm)    
  Autodesk.Revit.DB.Architecture RoomTagFilter

# See Also

[RoomTagFilter Members](c8b0c293-bb69-c045-0ce4-704fb54da5a1.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)