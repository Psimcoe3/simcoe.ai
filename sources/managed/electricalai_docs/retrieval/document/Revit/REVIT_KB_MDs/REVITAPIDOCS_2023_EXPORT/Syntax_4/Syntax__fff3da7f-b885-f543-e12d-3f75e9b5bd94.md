[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ConvertToIndependent Method

---



|  |
| --- |
| [View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Convert the dependent view to independent.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public void ConvertToIndependent() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub ConvertToIndependent ``` |

 

| Visual C++ |
| --- |
| ``` public: void ConvertToIndependent() ``` |

# Remarks

This method can be only applied to a dependent view. A dependent view can be created from another view using method View.Duplicate(ViewDuplicateOption.AsDependent). Dependent views have a valid primary view element ID that can be obtained via method View.GetPrimaryViewId(); Independent views have InvalidElementId as their primary view ID.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
public void MakeViewIndependent(View view)
{
    // Independent views will have an InvalidElementId for the Primary View Id
    if (view.GetPrimaryViewId() != ElementId.InvalidElementId)
    {
        view.ConvertToIndependent();
    }
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Public Sub MakeViewIndependent(view As View)
    ' Independent views will have an InvalidElementId for the Primary View Id
    If view.GetPrimaryViewId() <> ElementId.InvalidElementId Then
        view.ConvertToIndependent()
    End If
End Sub
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This view is not dependent. |

# See Also

[View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)