[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FamilyInstanceFilter Class

---



|  |
| --- |
| [Members](0ab03be9-6cb6-27b2-32b1-25057f96492e.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

A filter used to find elements that are family instances of the given family symbol.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public class FamilyInstanceFilter : ElementSlowFilter ``` |

 

| Visual Basic |
| --- |
| ``` Public Class FamilyInstanceFilter _ 	Inherits ElementSlowFilter ``` |

 

| Visual C++ |
| --- |
| ``` public ref class FamilyInstanceFilter : public ElementSlowFilter ``` |

# Remarks

This filter is a slow filter, but it uses a quick filter to eliminate non-candidate elements before the elements are obtained and expanded. Therefore this filter does not have to be paired with another quick filter to minimize the number of Elements that are expanded.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
// Creates a FamilyInstance filter for elements that are family instances of the given family symbol in the document

// Find all family symbols whose name is "W10X49"
FilteredElementCollector collector = new FilteredElementCollector(document);
collector = collector.OfClass(typeof(FamilySymbol));

// Get Element Id for family symbol which will be used to find family instances
var query = from element in collector where element.Name == "W10X49" select element;
List<Element> famSyms = query.ToList<Element>();
ElementId symbolId = famSyms[0].Id;

// Create a FamilyInstance filter with the FamilySymbol Id
FamilyInstanceFilter filter = new FamilyInstanceFilter(document, symbolId);

// Apply the filter to the elements in the active document
collector = new FilteredElementCollector(document);
ICollection<Element> familyInstances = collector.WherePasses(filter).ToElements();
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
' Creates a FamilyInstance filter for elements that are family instances of the given family symbol in the document


' Find all family symbols whose name is "W10X49"
Dim collector As New FilteredElementCollector(document)
collector = collector.OfClass(GetType(FamilySymbol))

' Get Element Id for family symbol which will be used to find family instances
Dim query As System.Collections.Generic.IEnumerable(Of Autodesk.Revit.DB.Element)
query = From element In collector _
 Where element.Name = "Level 1" _
 Select element

Dim famSyms As List(Of Element) = query.ToList()
Dim symbolId As ElementId = famSyms(0).Id

' Create a FamilyInstance filter with the FamilySymbol Id
Dim filter As New FamilyInstanceFilter(document, symbolId)

' Apply the filter to the elements in the active document
collector = New FilteredElementCollector(document)
Dim familyInstances As ICollection(Of Element) = collector.WherePasses(filter).ToElements()
```

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)    
  [Autodesk.Revit.DB ElementSlowFilter](e06b1e14-dd8d-8137-74ac-8ac4929eee85.htm)    
  Autodesk.Revit.DB FamilyInstanceFilter

# See Also

[FamilyInstanceFilter Members](0ab03be9-6cb6-27b2-32b1-25057f96492e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)