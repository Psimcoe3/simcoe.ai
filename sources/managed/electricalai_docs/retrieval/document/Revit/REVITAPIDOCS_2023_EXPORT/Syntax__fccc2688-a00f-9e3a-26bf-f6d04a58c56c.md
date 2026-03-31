[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ReferenceWithContext Class

---



|  |
| --- |
| [Members](f0db2af3-143a-3835-3aa1-c94e3ae93f61.htm)   [See Also](#seeAlsoToggle) |

An object including a reference to a geometric object and related context, as instance transform etc.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public class ReferenceWithContext : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ReferenceWithContext _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ReferenceWithContext : IDisposable ``` |

# Remarks

The ReferenceWithContext is used as the returned value from the method  [!:Autodesk::Revit::DB::Document::FindReferencesWithContextByDirection]  , ReferenceIntersector.Find(XYZ, XYZ), or ReferenceIntersector.FindNearest(XYZ, XYZ). It includes a reference intersecting a line extended in a certain direction from an origin point and the context of the geometric object, as the transform and proximity.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB ReferenceWithContext

# See Also

[ReferenceWithContext Members](f0db2af3-143a-3835-3aa1-c94e3ae93f61.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)