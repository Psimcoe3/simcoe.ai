[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Transform1D Class

---



|  |
| --- |
| [Members](a9b5b555-6085-c3d3-9413-61b1bcf17e70.htm)   [See Also](#seeAlsoToggle) |

An affine transform of 1D Euclidean space.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public class Transform1D : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class Transform1D _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class Transform1D : IDisposable ``` |

# Remarks

An affine transform is a linear transform plus a translation (which may be zero). 1D space is tranformed according to the following formula: t -> A\*t + B where A and B are constants. Some functions only accept certain kinds of transform (e.g., rigid motion, conformal, non-singular, etc.).

# Inheritance Hierarchy

System Object    
  Autodesk.Revit.DB Transform1D

# See Also

[Transform1D Members](a9b5b555-6085-c3d3-9413-61b1bcf17e70.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)