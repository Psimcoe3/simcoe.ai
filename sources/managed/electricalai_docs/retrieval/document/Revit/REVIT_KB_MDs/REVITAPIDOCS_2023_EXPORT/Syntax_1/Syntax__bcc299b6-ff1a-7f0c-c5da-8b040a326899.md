[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ConicalSurface Class

---



|  |
| --- |
| [Members](6de1bf03-7f30-32b8-e1d3-fd8c8eed0b89.htm)   [See Also](#seeAlsoToggle) |

A Conical Surface.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public class ConicalSurface : Surface ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ConicalSurface _ 	Inherits Surface ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ConicalSurface : public Surface ``` |

# Remarks

The parametric equation of the cone is S(u, v) = center + v\*[sin(halfAngle)(cos(u)\*xVec + sin(u)\*yVec) + cos(halfAngle)\*zVec]. Only the branch of the cone with v >= 0 should be used.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Surface](bb391358-5ca0-578d-e8e2-6d1b30c472d8.htm)    
  Autodesk.Revit.DB ConicalSurface

# See Also

[ConicalSurface Members](6de1bf03-7f30-32b8-e1d3-fd8c8eed0b89.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)