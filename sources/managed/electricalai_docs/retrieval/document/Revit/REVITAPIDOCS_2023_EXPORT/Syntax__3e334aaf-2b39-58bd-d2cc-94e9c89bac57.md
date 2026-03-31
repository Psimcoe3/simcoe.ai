[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LogicalAndFilter Class

---



|  |
| --- |
| [Members](1b21d9d2-f07a-d092-a5e5-ed151ae6fb1c.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

A filter that contains a set of filters. The filter passes when all filters in the set pass.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public class LogicalAndFilter : ElementLogicalFilter ``` |

 

| Visual Basic |
| --- |
| ``` Public Class LogicalAndFilter _ 	Inherits ElementLogicalFilter ``` |

 

| Visual C++ |
| --- |
| ``` public ref class LogicalAndFilter : public ElementLogicalFilter ``` |

# Remarks

The component filters may be reordered by Revit to cause the quickest acting filters to be evaluated first.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
// Find all door instances in the project by finding all elements that both belong to the door 
// category and are family instances.
ElementClassFilter familyInstanceFilter = new ElementClassFilter(typeof(FamilyInstance));

// Create a category filter for Doors
ElementCategoryFilter doorsCategoryfilter = new ElementCategoryFilter(BuiltInCategory.OST_Doors);

// Create a logic And filter for all Door FamilyInstances
LogicalAndFilter doorInstancesFilter = new LogicalAndFilter(familyInstanceFilter, doorsCategoryfilter);

// Apply the filter to the elements in the active document
FilteredElementCollector collector = new FilteredElementCollector(document);
IList<Element> doors = collector.WherePasses(doorInstancesFilter).ToElements();
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
' Find all door instances in the project by finding all elements that both belong to the door 
' category and are family instances.
Dim familyInstanceFilter As New ElementClassFilter(GetType(FamilyInstance))

' Create a category filter for Doors
Dim doorsCategoryfilter As New ElementCategoryFilter(BuiltInCategory.OST_Doors)

' Create a logic And filter for all Door FamilyInstances
Dim doorInstancesFilter As New LogicalAndFilter(familyInstanceFilter, doorsCategoryfilter)

' Apply the filter to the elements in the active document
Dim collector As New FilteredElementCollector(document)
Dim doors As IList(Of Element) = collector.WherePasses(doorInstancesFilter).ToElements()
```

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)    
  [Autodesk.Revit.DB ElementLogicalFilter](3b8d6b55-0cab-1810-1188-840800e5eaa2.htm)    
  Autodesk.Revit.DB LogicalAndFilter

# See Also

[LogicalAndFilter Members](1b21d9d2-f07a-d092-a5e5-ed151ae6fb1c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)