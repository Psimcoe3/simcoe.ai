[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Workset Class

---



|  |
| --- |
| [Members](437250cb-c87d-4492-9a53-bde8605012f4.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Represents a workset in the document.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public class Workset : WorksetPreview ``` |

 

| Visual Basic |
| --- |
| ``` Public Class Workset _ 	Inherits WorksetPreview ``` |

 

| Visual C++ |
| --- |
| ``` public ref class Workset : public WorksetPreview ``` |

# Remarks

Worksets are a way to divide a set of elements in the Revit document into subsets for worksharing. There may be one or many worksets in a document. Each element in the document must belong to one and only one workset.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
public Workset GetActiveWorkset(Document doc)
{
    // Get the workset table from the document
    WorksetTable worksetTable = doc.GetWorksetTable();
    // Get the Id of the active workset
    WorksetId activeId = worksetTable.GetActiveWorksetId();
    // Find the workset with that Id 
    Workset workset = worksetTable.GetWorkset(activeId);
    return workset;
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Public Function GetActiveWorkset(doc As Document) As Workset
    ' Get the workset table from the document
    Dim worksetTable As WorksetTable = doc.GetWorksetTable()
    ' Get the Id of the active workset
    Dim activeId As WorksetId = worksetTable.GetActiveWorksetId()
    ' Find the workset with that Id 
    Dim workset As Workset = worksetTable.GetWorkset(activeId)
    Return workset
End Function
```

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB WorksetPreview](5091902c-a286-eb9e-d65b-3d421d741c69.htm)    
  Autodesk.Revit.DB Workset

# See Also

[Workset Members](437250cb-c87d-4492-9a53-bde8605012f4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)