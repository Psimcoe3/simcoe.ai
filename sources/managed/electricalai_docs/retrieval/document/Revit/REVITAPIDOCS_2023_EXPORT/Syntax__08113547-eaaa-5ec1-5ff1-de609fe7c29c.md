[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DisplacementElement Class

---



|  |
| --- |
| [Members](b22d4d89-022c-ea70-fc2d-868679609d72.htm)   [See Also](#seeAlsoToggle) |

A view-specific element that causes other elements to appear to be displaced from their actual locations.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public class DisplacementElement : Element ``` |

 

| Visual Basic |
| --- |
| ``` Public Class DisplacementElement _ 	Inherits Element ``` |

 

| Visual C++ |
| --- |
| ``` public ref class DisplacementElement : public Element ``` |

# Remarks

The DisplacementElement does not actually change the location of any model elements; it merely causes them to be displayed in a different location.

An element may only be displaced by a single DisplacementElement in any view. Assigning an element to more than one DisplacementElement is an error condition.

A DisplacementElement can declare another DisplacementElement as its parent. In that case, its transform will be concatenated with that of the parent, and the displacement of its associated elements will be relative to the parent DisplacementElement.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  Autodesk.Revit.DB DisplacementElement

# See Also

[DisplacementElement Members](b22d4d89-022c-ea70-fc2d-868679609d72.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)