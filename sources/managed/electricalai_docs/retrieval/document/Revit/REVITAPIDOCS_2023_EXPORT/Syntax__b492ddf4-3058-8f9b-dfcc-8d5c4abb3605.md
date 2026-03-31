[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ElementCategoryFilter Class

---



|  |
| --- |
| [Members](6b8f4e3a-1975-7388-3848-462cf305d523.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

A filter used to match elements by their category.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public class ElementCategoryFilter : ElementQuickFilter ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ElementCategoryFilter _ 	Inherits ElementQuickFilter ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ElementCategoryFilter : public ElementQuickFilter ``` |

# Remarks

This filter is a quick filter. Quick filters operate only on the ElementRecord, a low-memory class which has a limited interface to read element properties. Elements which are rejected by a quick filter will not be expanded in memory.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
// Find all Wall instances in the document by using category filter
ElementCategoryFilter filter = new ElementCategoryFilter(BuiltInCategory.OST_Walls);

// Apply the filter to the elements in the active document,
// Use shortcut WhereElementIsNotElementType() to find wall instances only
FilteredElementCollector collector = new FilteredElementCollector(document);
IList<Element> walls = collector.WherePasses(filter).WhereElementIsNotElementType().ToElements();
String prompt = "The walls in the current document are:\n";
foreach (Element e in walls)
{
    prompt += e.Name + "\n";
}
TaskDialog.Show("Revit", prompt);
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
' Find all Wall instances in the document by using category filter
Dim filter As New ElementCategoryFilter(BuiltInCategory.OST_Walls)

' Apply the filter to the elements in the active document,
' Use shortcut WhereElementIsNotElementType() to find wall instances only
Dim collector As New FilteredElementCollector(document)
Dim walls As IList(Of Element) = collector.WherePasses(filter).WhereElementIsNotElementType().ToElements()
Dim prompt As [String] = "The walls in the current document are:" & vbLf
For Each e As Element In walls
    prompt += e.Name + vbLf
Next
TaskDialog.Show("Revit", prompt)
```

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)    
  [Autodesk.Revit.DB ElementQuickFilter](ebc95d82-11fc-69f6-2df1-52331dd36443.htm)    
  Autodesk.Revit.DB ElementCategoryFilter

# See Also

[ElementCategoryFilter Members](6b8f4e3a-1975-7388-3848-462cf305d523.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)