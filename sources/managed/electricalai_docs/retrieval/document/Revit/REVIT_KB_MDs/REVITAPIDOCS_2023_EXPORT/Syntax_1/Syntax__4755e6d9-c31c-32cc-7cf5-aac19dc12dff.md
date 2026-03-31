[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetActiveWorksetId Method

---



|  |
| --- |
| [WorksetTable Class](9ffa5fc8-e6a5-17d6-590e-8ecbfd7b85fb.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Returns the active workset's WorksetId.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public WorksetId GetActiveWorksetId() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetActiveWorksetId As WorksetId ``` |

 

| Visual C++ |
| --- |
| ``` public: WorksetId^ GetActiveWorksetId() ``` |

#### Return Value

WorksetId of the active workset.

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

# See Also

[WorksetTable Class](9ffa5fc8-e6a5-17d6-590e-8ecbfd7b85fb.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)