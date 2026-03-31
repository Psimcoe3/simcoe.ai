[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DirectShapeLibrary Class

---



|  |
| --- |
| [Members](a37160c8-6f87-cdd4-e772-5ef618363edc.htm)   [See Also](#seeAlsoToggle) |

DirectShapeLibrary is used to store pre-created geometry for further referencing via the definition/instance mechanism. It is not persistent: the scope of a library object is usually a single data creation session. DirectShape::createGeometryInstance and DirectShape::CreateElementInstance will use the current DirectShapeLibrary to look up the definitions. store a collection of GNodes as definition end class DirectShapeDefinition

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public class DirectShapeLibrary : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class DirectShapeLibrary _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class DirectShapeLibrary : IDisposable ``` |

# Remarks

There are two ways to add a definition to the library. The first is to add the definition as an array of geometry objects. A DirectShape created as an instance of that definition will hold a copy of predefined geometry, transformed as requested. If the definition was added as a DirectShapeType, a DirectShape object created as an instance of that definition will reference the type. Its geometry would be an instance of type geometry.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB DirectShapeLibrary

# See Also

[DirectShapeLibrary Members](a37160c8-6f87-cdd4-e772-5ef618363edc.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)