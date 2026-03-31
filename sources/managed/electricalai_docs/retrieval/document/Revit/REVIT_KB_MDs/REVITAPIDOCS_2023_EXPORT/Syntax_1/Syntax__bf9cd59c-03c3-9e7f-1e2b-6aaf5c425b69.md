[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Mesh Class

---



|  |
| --- |
| [Members](73c32522-8475-2aeb-4e2a-401b1f699425.htm)   [See Also](#seeAlsoToggle) |

A triangular mesh.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)

# Syntax

| C# |
| --- |
| ``` public class Mesh : GeometryObject ``` |

 

| Visual Basic |
| --- |
| ``` Public Class Mesh _ 	Inherits GeometryObject ``` |

 

| Visual C++ |
| --- |
| ``` public ref class Mesh : public GeometryObject ``` |

# Remarks

Meshes are generated during triangulation of faces. They can also be encountered directly in Revit geometry (typically imported geometry). Meshes contain a single array of  [Vertices](32b34134-9301-f952-a910-5a34d0d0235d.htm)  , and a corresponding array of triangles. Triangles can be accessed by index from  [Triangle Int32](35abd642-cf15-8281-e45d-083fb5c53d2a.htm)  , and reference 3 vertices from the  [Vertices](32b34134-9301-f952-a910-5a34d0d0235d.htm)  array.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm)    
  [Autodesk.Revit.DB GeometryObject](e0f15010-0e19-6216-e2f0-ab7978145daa.htm)    
  Autodesk.Revit.DB Mesh

# See Also

[Mesh Members](73c32522-8475-2aeb-4e2a-401b1f699425.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)