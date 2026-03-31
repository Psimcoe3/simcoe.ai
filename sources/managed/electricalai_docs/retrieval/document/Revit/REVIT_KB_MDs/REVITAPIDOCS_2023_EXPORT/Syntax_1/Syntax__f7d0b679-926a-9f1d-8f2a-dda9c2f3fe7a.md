[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BRepBuilderGeometryId Class

---



|  |
| --- |
| [Members](3f1a3fb9-60a8-fe52-8ec4-28d078096e9b.htm)   [See Also](#seeAlsoToggle) |

This class is used by the BRepBuilder class to identify objects it creates (faces, edges, etc.).

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public class BRepBuilderGeometryId : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class BRepBuilderGeometryId _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class BRepBuilderGeometryId : IDisposable ``` |

# Remarks

The user should use these ids to organize the calls to BRepBuilder methods (e.g., addLoop() takes a face id as input, referring to a face that was previously added by a call to AddFace()). The ids are only valid while the BRepBuilder is in use.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB BRepBuilderGeometryId

# See Also

[BRepBuilderGeometryId Members](3f1a3fb9-60a8-fe52-8ec4-28d078096e9b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)