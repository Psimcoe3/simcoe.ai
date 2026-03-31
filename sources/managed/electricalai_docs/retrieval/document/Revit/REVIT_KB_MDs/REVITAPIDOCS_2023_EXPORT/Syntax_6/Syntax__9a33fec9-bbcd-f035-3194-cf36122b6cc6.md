[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RuledSurface Class

---



|  |
| --- |
| [Members](02204fae-ae70-33ea-2f6c-28b40dea2ca6.htm)   [See Also](#seeAlsoToggle) |

A ruled surface is created by sweeping a line between two profile curves or between a curve and a point (a point and a curve). Input curve(s) must be bounded or have natural bounds.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public class RuledSurface : Surface ``` |

 

| Visual Basic |
| --- |
| ``` Public Class RuledSurface _ 	Inherits Surface ``` |

 

| Visual C++ |
| --- |
| ``` public ref class RuledSurface : public Surface ``` |

# Remarks

Both curves are evaluated in normalized parameters [0, 1] The parametric equations of a ruled surface are: C1 != 0 and C2 != 0 : S(u, v) = C1(u) + v \* (C2(u) - C1(u)); C2 == 0 and C1 != 0 : S(u, v) = P1 + v \* (C2(u) - P1); C1 == 0 and C2 != 0 : S(u, v) = C1(u) + v \* (P2 - C1(u)); C1 == 0 and C2 == 0 - is not allowed as that would define a degenerate ruled surface.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Surface](bb391358-5ca0-578d-e8e2-6d1b30c472d8.htm)    
  Autodesk.Revit.DB RuledSurface

# See Also

[RuledSurface Members](02204fae-ae70-33ea-2f6c-28b40dea2ca6.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)