[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### InsertRow Method

---



|  |
| --- |
| [TableSectionData Class](a0e6f821-5f53-1eb0-eba1-16554b3c0dc8.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Inserts a row data at a specified index.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public void InsertRow( 	int nIndex ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub InsertRow ( _ 	nIndex As Integer _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void InsertRow( 	int nIndex ) ``` |

#### Parameters

nIndex
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     An integer index.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
public void CreateSubtitle(ViewSchedule schedule)
{
    TableData colTableData = schedule.GetTableData();

    TableSectionData tsd = colTableData.GetSectionData(SectionType.Header);
    tsd.InsertRow(tsd.FirstRowNumber + 1);
    tsd.SetCellText(tsd.FirstRowNumber + 1, tsd.FirstColumnNumber, "Schedule of column top and base levels with offsets");
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Public Sub CreateSubtitle(schedule As ViewSchedule)
    Dim colTableData As TableData = schedule.GetTableData()

    Dim tsd As TableSectionData = colTableData.GetSectionData(SectionType.Header)
    tsd.InsertRow(tsd.FirstRowNumber + 1)
    tsd.SetCellText(tsd.FirstRowNumber + 1, tsd.FirstColumnNumber, "Schedule of column top and base levels with offsets")
End Sub
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The row can't be inserted in data section of standard schedule except Key Schedule, Sheet List Schedule or following categories without emdeded schedule: MEP Space, Room, Area. or nIndex is invalid index. |

# See Also

[TableSectionData Class](a0e6f821-5f53-1eb0-eba1-16554b3c0dc8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)