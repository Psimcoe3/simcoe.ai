[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetTypeId Method

---



|  |
| --- |
| [Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Returns the identifier of this element's type.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public ElementId GetTypeId() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetTypeId As ElementId ``` |

 

| Visual C++ |
| --- |
| ``` public: ElementId^ GetTypeId() ``` |

#### Return Value

The id of the element's type, or invalid element id if the element cannot have type assigned.

# Remarks

Some elements cannot have type assigned, in which case this method returns invalid element id.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
void GetStairType(Autodesk.Revit.DB.Document document)
{
   FilteredElementCollector collector = new FilteredElementCollector(document);
   ICollection<Element> stairs = collector.OfClass(typeof(FamilyInstance)).OfCategory(BuiltInCategory.OST_Stairs).ToElements();
   foreach (Element stair in stairs)
    {
        if (null == stair.GetTypeId())
        {
            TaskDialog.Show("Revit","No symbol found in stair element: " + stair.Name);
        }
        else
        {
            Element elemType = document.GetElement(stair.GetTypeId());
            string info = "Stair type is: " + elemType.Name;
            TaskDialog.Show("Revit",info);
        }
    }
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Sub GetStairType(document As Autodesk.Revit.DB.Document)
    Dim collector As New FilteredElementCollector(document)
    Dim stairs As ICollection(Of Element) = collector.OfClass(GetType(FamilyInstance)).OfCategory(BuiltInCategory.OST_Stairs).ToElements()
    For Each stair As Element In stairs
        If stair.GetTypeId() Is Nothing Then
            TaskDialog.Show("Revit", "No symbol found in stair element: " + stair.Name)
        Else
            Dim elemType As Element = document.GetElement(stair.GetTypeId())
            Dim info As String = "Stair type is: " + elemType.Name
            TaskDialog.Show("Revit", info)
        End If
    Next
End Sub
```

# See Also

[Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)