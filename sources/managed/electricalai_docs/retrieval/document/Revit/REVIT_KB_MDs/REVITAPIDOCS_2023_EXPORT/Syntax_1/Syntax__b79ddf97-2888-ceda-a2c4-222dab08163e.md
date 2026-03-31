[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ConceptualSurfaceType Class

---



|  |
| --- |
| [Members](025f7279-238b-94c3-38ee-43fdd312b81c.htm)   [See Also](#seeAlsoToggle) |

This element represents a conceptual BIM object category to assign to faces in Mass geometries. There is one ConceptualSurfaceType element for each of the Mass Surface Subcategories. for serialization

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public class ConceptualSurfaceType : Element ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ConceptualSurfaceType _ 	Inherits Element ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ConceptualSurfaceType : public Element ``` |

# Remarks

When Conceptual Energy Analysis is enabled in Revit Projects, massing faces will be assigned to the subcategories of Mass category that these ConceptualSurfaceType's are associated with. A default ConceptualConstructionType is associated with the ConceptualSurfaceType. This default ConceptualConstructionType is assigned to Mass faces with the corresponding subcategory. Changing the default ConceptualConstructionType associated with the ConceptualSurfaceType will update the ConceptualConstruction type for all Mass faces of that subcategory which the user has not specifically provided an override value for.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  Autodesk.Revit.DB.Analysis ConceptualSurfaceType

# See Also

[ConceptualSurfaceType Members](025f7279-238b-94c3-38ee-43fdd312b81c.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)