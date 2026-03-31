[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IExternalCommandAvailability Interface

---



|  |
| --- |
| [Members](30f3d4bd-c1f1-dd4c-bdc0-5325b591aed7.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

An interface that should be implemented to provide the implementation for a accessibility check for a Revit add-in External Command.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 23.0.0.0 (23.1.0.0)

# Syntax

| C# |
| --- |
| ``` public interface IExternalCommandAvailability ``` |

 

| Visual Basic |
| --- |
| ``` Public Interface IExternalCommandAvailability ``` |

 

| Visual C++ |
| --- |
| ``` public interface class IExternalCommandAvailability ``` |

# Remarks

This interface should share the same assembly with add-in External Command.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
public class SampleAccessibilityCheck : IExternalCommandAvailability
{
    public bool IsCommandAvailable(Autodesk.Revit.UI.UIApplication applicationData, 
        CategorySet selectedCategories)
    {
        // Allow button click if there is no active selection
        if (selectedCategories.IsEmpty)
            return true;
        // Allow button click if there is at least one wall selected
        foreach (Category c in selectedCategories)
        {
            if (c.BuiltInCategory == BuiltInCategory.OST_Walls)
                return true;
        }
        return false;
    }
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Public Class SampleAccessibilityCheck
    Implements IExternalCommandAvailability
    Public Function IsCommandAvailable(applicationData As Autodesk.Revit.UI.UIApplication, selectedCategories As CategorySet) As Boolean Implements IExternalCommandAvailability.IsCommandAvailable
        ' Allow button click if there is no active selection
        If selectedCategories.IsEmpty Then
            Return True
        End If
        ' Allow button click if there is at least one wall selected
        For Each c As Category In selectedCategories
            If c.BuiltInCategory = BuiltInCategory.OST_Walls Then
                Return True
            End If
        Next
        Return False
    End Function
End Class
```

# See Also

[IExternalCommandAvailability Members](30f3d4bd-c1f1-dd4c-bdc0-5325b591aed7.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)