[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ElementClassFilter Class

---



|  |
| --- |
| [Members](e19b753f-8d74-0a9c-b8aa-65809418ff97.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

A filter used to match elements by their class.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public class ElementClassFilter : ElementQuickFilter ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ElementClassFilter _ 	Inherits ElementQuickFilter ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ElementClassFilter : public ElementQuickFilter ``` |

# Remarks

This filter is a quick filter. Quick filters operate only on the ElementRecord, a low-memory class which has a limited interface to read element properties. Elements which are rejected by a quick filter will not be expanded in memory.

This filter will match elements whose class is an exact match to the input class, or elements whose class is derived from the input class.

There is a small subset of Element subclasses in the API which are not supported by this filter. These types exist in the API, but not in Revit's native object model, which means that this filter doesn't support them. In order to use a class filter to find elements of these types, it is necessary to use a higher level class and then process the results further to find elements matching only the subtype. The following types are affected by this restriction:

* Subclasses of Autodesk.Revit.DB.Material
* Subclasses of Autodesk.Revit.DB.CurveElement
* Subclasses of Autodesk.Revit.DB.ConnectorElement
* Subclasses of Autodesk.Revit.DB.HostedSweep
* Autodesk.Revit.DB.Architecture.Room
* Autodesk.Revit.DB.Mechanical.Space
* Autodesk.Revit.DB.Area
* Autodesk.Revit.DB.Architecture.RoomTag
* Autodesk.Revit.DB.Mechanical.SpaceTag
* Autodesk.Revit.DB.AreaTag
* Autodesk.Revit.DB.CombinableElement
* Autodesk.Revit.DB.Mullion
* Autodesk.Revit.DB.Panel
* Autodesk.Revit.DB.AnnotationSymbol
* Autodesk.Revit.DB.Structure.AreaReinforcementType
* Autodesk.Revit.DB.Structure.PathReinforcementType
* Autodesk.Revit.DB.AnnotationSymbolType
* Autodesk.Revit.DB.Architecture.RoomTagType
* Autodesk.Revit.DB.Mechanical.SpaceTagType
* Autodesk.Revit.DB.AreaTagType
* Autodesk.Revit.DB.Structure.TrussType

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
// Use ElementClassFilter to find family instances whose name is 60" x 30" Student 
ElementClassFilter filter = new ElementClassFilter(typeof(FamilyInstance));

// Apply the filter to the elements in the active document
FilteredElementCollector collector = new FilteredElementCollector(document);
collector.WherePasses(filter);

// Use Linq query to find family instances whose name is 60" x 30" Student
var query = from element in collector
            where element.Name == "60\" x 30\" Student"
            select element;

// Cast found elements to family instances, 
// this cast to FamilyInstance is safe because ElementClassFilter for FamilyInstance was used
List<FamilyInstance> familyInstances = query.Cast<FamilyInstance>().ToList<FamilyInstance>();
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
' Use ElementClassFilter to find family instances whose name is 60" x 30" Student 
Dim filter As New ElementClassFilter(GetType(FamilyInstance))

' Apply the filter to the elements in the active document
Dim collector As New FilteredElementCollector(document)
collector.WherePasses(filter)

' Use Linq query to find family instances whose name is 60" x 30" Student
Dim query As System.Collections.Generic.IEnumerable(Of Autodesk.Revit.DB.Element)
query = From element In collector _
 Where element.Name = "60"" x 30"" Student" _
 Select element

' Cast found elements to family instances, 
' this cast to FamilyInstance is safe because ElementClassFilter for FamilyInstance was used
Dim familyInstances As List(Of FamilyInstance) = query.Cast(Of FamilyInstance)().ToList()
```

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)    
  [Autodesk.Revit.DB ElementQuickFilter](ebc95d82-11fc-69f6-2df1-52331dd36443.htm)    
  Autodesk.Revit.DB ElementClassFilter

# See Also

[ElementClassFilter Members](e19b753f-8d74-0a9c-b8aa-65809418ff97.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)