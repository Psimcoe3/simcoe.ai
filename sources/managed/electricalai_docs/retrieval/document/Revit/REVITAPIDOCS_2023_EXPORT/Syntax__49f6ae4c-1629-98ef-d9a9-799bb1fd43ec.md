[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Form Class

---



|  |
| --- |
| [Members](6996b66a-bd53-636c-cba5-5a651b36ab53.htm)   [See Also](#seeAlsoToggle) |

An object that represents a Form within the Autodesk Revit Massing Family.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class Form : GenericForm ``` |

 

| Visual Basic |
| --- |
| ``` Public Class Form _ 	Inherits GenericForm ``` |

 

| Visual C++ |
| --- |
| ``` public ref class Form : public GenericForm ``` |

# Remarks

For any reference returned from a Form method, its GeometryObject will become invalid after a form modification method, e.g. MoveSubElement. Call the method on the Form object to retrieve the new reference if it is needed after the modification.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  [Autodesk.Revit.DB CombinableElement](c88bdbbc-dbbb-0817-a358-35f8686f68a2.htm)    
  [Autodesk.Revit.DB GenericForm](d64cecab-ceec-407e-6f09-0b83f192aa1a.htm)    
  Autodesk.Revit.DB Form

# See Also

[Form Members](6996b66a-bd53-636c-cba5-5a651b36ab53.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)