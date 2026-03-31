[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarShapeDrivenAccessor Class

---



|  |
| --- |
| [Members](f7f7f744-3ddd-1572-b36f-acf1e26b2ea9.htm)   [See Also](#seeAlsoToggle) |

A class that is used to access the properties and capabilities of shape-driven Rebar.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public class RebarShapeDrivenAccessor : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class RebarShapeDrivenAccessor _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class RebarShapeDrivenAccessor : IDisposable ``` |

# Remarks

Obtain an instance of this class from  [GetShapeDrivenAccessor](c77085bd-db18-4869-bb2a-1e5c702e273a.htm)  . The accessor includes a reference to the Rebar element. If the referenced Rebar element is deleted, using the methods form this class will throw exception.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB.Structure RebarShapeDrivenAccessor

# See Also

[RebarShapeDrivenAccessor Members](f7f7f744-3ddd-1572-b36f-acf1e26b2ea9.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)