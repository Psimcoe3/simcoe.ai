[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TriangulationInterfaceForTriangulatedSolidOrShell Class

---



|  |
| --- |
| [Members](95d11396-e82c-aa34-816a-7fe27374004d.htm)   [See Also](#seeAlsoToggle) |

This class is used to call FacetingUtils::convertTrianglesToQuads with a triangulation defined by a TriangulatedSolidOrShell.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public class TriangulationInterfaceForTriangulatedSolidOrShell : TriangulationInterface ``` |

 

| Visual Basic |
| --- |
| ``` Public Class TriangulationInterfaceForTriangulatedSolidOrShell _ 	Inherits TriangulationInterface ``` |

 

| Visual C++ |
| --- |
| ``` public ref class TriangulationInterfaceForTriangulatedSolidOrShell : public TriangulationInterface ``` |

# Remarks

The vertex and triangle indices used by this class treat the triangulated solid or shell as if all the vertices and triangles of the different shell components were collected into single sets of vertices and triangles, respectively. For example, if a solid has two shell components and the first has ten vertices while the second has five vertices, vertexIndex 6 refers to vertex[6] of the first shell component, and vertexIndex 12 refers to vertex[2] of the second shell component. You can use the class TriangulationInterfaceForTriangulatedShellComponent to get a faceting of an individual shell component.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB TriangulationInterface](52c77543-3282-78a8-6a57-dd245b2090c4.htm)    
  Autodesk.Revit.DB TriangulationInterfaceForTriangulatedSolidOrShell

# See Also

[TriangulationInterfaceForTriangulatedSolidOrShell Members](95d11396-e82c-aa34-816a-7fe27374004d.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)