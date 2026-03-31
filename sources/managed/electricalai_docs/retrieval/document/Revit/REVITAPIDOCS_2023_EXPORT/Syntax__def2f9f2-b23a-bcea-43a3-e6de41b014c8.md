[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BoundingBox Property

---



|  |
| --- |
| [Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Retrieves a box that circumscribes all geometry of the element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)

# Syntax

| C# |
| --- |
| ``` public BoundingBoxXYZ this[ 	View A_0 ] { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property BoundingBox ( _ 	A_0 As View _ ) As BoundingBoxXYZ 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property BoundingBoxXYZ^ BoundingBox[View^ A_0] { 	BoundingBoxXYZ^ get (View^ A_0); } ``` |

#### Parameters

A\_0
:   Type:  [Autodesk.Revit.DB View](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)

# Remarks

Pass in a view to query view-specific (e.g., cut) geometry or    a null reference (  Nothing  in Visual Basic)  for model geometry. If the view box is not known or cannot be calculated, this will return the model box; if the model box is not known, this will return    a null reference (  Nothing  in Visual Basic)  . The box will always be aligned to the default axes of the model coordinate system (thus no rotation should be applied to the return value). Also note that this bounding box volume may enclose geometry that is not obvious. For example, the "flip controls" that could be part of a family will be included in the computation of the bounding box even though they are not always visible in the family instance of the family.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
private void GetElementBoundingBox(Autodesk.Revit.DB.Document document, Autodesk.Revit.DB.Element element)
{
    // Get the BoundingBox instance for current view.
    BoundingBoxXYZ box = element.get_BoundingBox(document.ActiveView);
    if (null == box)
    {
        throw new Exception("Selected element doesn't contain a bounding box.");
    }

    string info = "Bounding box is enabled: " + box.Enabled.ToString();

    // Give the user some information.
    TaskDialog.Show("Revit",info);
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Sub GetElementBoundingBox(document As Autodesk.Revit.DB.Document, element As Autodesk.Revit.DB.Element)
    ' Get the BoundingBox instance for current view.
    Dim box As BoundingBoxXYZ = element.BoundingBox(document.ActiveView)
    If box Is Nothing Then
        Throw New Exception("Selected element doesn't contain a bounding box.")
    End If

    Dim info As String = "Bounding box is enabled: " & box.Enabled.ToString()

    ' Give the user some information.
    TaskDialog.Show("Revit", info)
End Sub
```

# See Also

[Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)