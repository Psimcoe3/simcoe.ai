[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BoundingBoxContainsPointFilter Class

---



|  |
| --- |
| [Members](96e67c60-1829-5d15-b308-7ea8e69b3990.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

A filter used to match elements with a bounding box that contains the given point.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public class BoundingBoxContainsPointFilter : ElementQuickFilter ``` |

 

| Visual Basic |
| --- |
| ``` Public Class BoundingBoxContainsPointFilter _ 	Inherits ElementQuickFilter ``` |

 

| Visual C++ |
| --- |
| ``` public ref class BoundingBoxContainsPointFilter : public ElementQuickFilter ``` |

# Remarks

This filter excludes all objects derived from View and objects derived from ElementType. This filter is a quick filter. Quick filters operate only on the ElementRecord, a low-memory class which has a limited interface to read element properties. Elements which are rejected by a quick filter will not be expanded in memory.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
// Use BoundingBoxContainsPoint filter to find elements with a bounding box that contains the 
// given point in the document.

// Create a BoundingBoxContainsPoint filter for base point of (0, 0, 0)
XYZ basePnt = new XYZ(0, 0, 0);
BoundingBoxContainsPointFilter filter = new BoundingBoxContainsPointFilter(basePnt);

// Apply the filter to the elements in the active document
// This filter will excludes all objects derived from View and objects derived from ElementType
FilteredElementCollector collector = new FilteredElementCollector(document);
IList<Element> elements = collector.WherePasses(filter).ToElements();


// Find walls that do not contain the given point: use an inverted filter to match elements
// Use shortcut command OfClass() to find walls only
BoundingBoxContainsPointFilter notContainFilter =
    new BoundingBoxContainsPointFilter(basePnt, true); // inverted filter
collector = new FilteredElementCollector(document);
IList<Element> notContainFounds =
    collector.OfClass(typeof(Wall)).WherePasses(notContainFilter).ToElements();
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
' Use BoundingBoxContainsPoint filter to find elements with a bounding box that contains the 
' given point in the document.


' Create a BoundingBoxContainsPoint filter for base point of (0, 0, 0)
Dim basePnt As New XYZ(0, 0, 0)
Dim filter As New BoundingBoxContainsPointFilter(basePnt)

' Apply the filter to the elements in the active document
' This filter will excludes all objects derived from View and objects derived from ElementType
Dim collector As New FilteredElementCollector(document)
Dim elements As IList(Of Element) = collector.WherePasses(filter).ToElements()


' Find walls that do not contain the given point: use an inverted filter to match elements
' Use shortcut command OfClass() to find walls only
Dim notContainFilter As New BoundingBoxContainsPointFilter(basePnt, True)
' inverted filter
collector = New FilteredElementCollector(document)
Dim notContainFounds As IList(Of Element) = collector.OfClass(GetType(Wall)).WherePasses(notContainFilter).ToElements()
```

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)    
  [Autodesk.Revit.DB ElementQuickFilter](ebc95d82-11fc-69f6-2df1-52331dd36443.htm)    
  Autodesk.Revit.DB BoundingBoxContainsPointFilter

# See Also

[BoundingBoxContainsPointFilter Members](96e67c60-1829-5d15-b308-7ea8e69b3990.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)