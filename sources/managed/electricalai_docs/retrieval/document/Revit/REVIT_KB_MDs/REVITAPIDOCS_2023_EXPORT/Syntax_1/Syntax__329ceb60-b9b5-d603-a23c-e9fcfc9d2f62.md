[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SortParameters Method

---



|  |
| --- |
| [FamilyManager Class](1cc4fe6c-0e9f-7439-0021-32d2e06f4c33.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Sorts the family parameters according to the desired sort order.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public void SortParameters( 	ParametersOrder order ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SortParameters ( _ 	order As ParametersOrder _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SortParameters( 	ParametersOrder order ) ``` |

#### Parameters

order
:   Type:  [Autodesk.Revit.DB ParametersOrder](771bd717-9d4d-d36d-0948-94e2e73f392c.htm)    
     The desired sort order.

# Remarks

The sort only affects visible parameters within the same parameter group.

Parameters that belong to different groups will remain separated, and the groups' order will not be affected.

The sort is a one-time operation and when new parameters are added they will not be automatically sorted.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
private void DisplayParametersInAscendingOrder(Document familyDoc)
{
    FamilyManager familyManager = familyDoc.FamilyManager;
    familyManager.SortParameters(ParametersOrder.Ascending);
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Sub DisplayParametersInAscendingOrder(familyDoc As Document)
    Dim familyManager As FamilyManager = familyDoc.FamilyManager
    familyManager.SortParameters(ParametersOrder.Ascending)
End Sub
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when this family is a Rebar Shape family which doesn't support parameters reorder. |

# See Also

[FamilyManager Class](1cc4fe6c-0e9f-7439-0021-32d2e06f4c33.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)