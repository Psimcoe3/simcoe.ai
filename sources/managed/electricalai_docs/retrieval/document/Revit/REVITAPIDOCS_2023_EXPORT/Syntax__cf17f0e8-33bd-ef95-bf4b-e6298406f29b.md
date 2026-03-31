[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Entity Class

---



|  |
| --- |
| [Members](ce6988c7-4038-002c-70eb-75a38ec394b9.htm)   [See Also](#seeAlsoToggle) |

An object stored in the Extensible Storage framework. An Entity is described by a Schema, which serves both to identify an Entity, and to describe its contents (Fields).

**Namespace:**   [Autodesk.Revit.DB.ExtensibleStorage](79486a74-376c-9555-c873-45d5a750f051.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public class Entity : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class Entity _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class Entity : IDisposable ``` |

# Remarks

An Entity is similar to an object in most object-oriented languages, while a Schema is the class of that object. The Get and Set methods are central - they provide access to the fields of the Entity. Note that an unitialized Entity retrieved from an Element or another Entity (if it has not been created yet) will be represented as an invalid entity, not    a null reference (  Nothing  in Visual Basic)  . If an Element containing an Entity is split (e.g., a wall split), the Entity and its data will exist in both new Elements. If an Element containing an Entity is copied, the Element copy will also contain a copy of the Entity and its data. If an Entity stores an ElementId, and the Element with that ElementId is deleted, the stored ElementId will automatically be set to ElementId.InvalidElementId (-1).

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB.ExtensibleStorage Entity

# See Also

[Entity Members](ce6988c7-4038-002c-70eb-75a38ec394b9.htm)

[Autodesk.Revit.DB.ExtensibleStorage Namespace](79486a74-376c-9555-c873-45d5a750f051.htm)