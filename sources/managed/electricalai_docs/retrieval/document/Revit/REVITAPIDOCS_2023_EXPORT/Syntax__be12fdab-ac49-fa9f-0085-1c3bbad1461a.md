[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method

---



|  |
| --- |
| [StairsPath Class](ed5913d6-1219-9c7c-7e52-317dd58d7cd3.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Creates a new stairs path for the specified stairs with the specified stairs path type only in the plan view.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static StairsPath Create( 	Document document, 	LinkElementId stairsId, 	ElementId typeId, 	ElementId planViewId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	document As Document, _ 	stairsId As LinkElementId, _ 	typeId As ElementId, _ 	planViewId As ElementId _ ) As StairsPath ``` |

 

| Visual C++ |
| --- |
| ``` public: static StairsPath^ Create( 	Document^ document,  	LinkElementId^ stairsId,  	ElementId^ typeId,  	ElementId^ planViewId ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

stairsId
:   Type:  [Autodesk.Revit.DB LinkElementId](6e18abde-8787-9906-8576-ab0c9c5432c6.htm)    
     The id of the stairs element either in the host document or in a linked document.

typeId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The type of stairs path.

planViewId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The plan view in which the stairs path will be shown.

#### Return Value

The new stairs path.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
private void CreateStairsPath(Document document, Stairs stairs)
{
    Transaction transNewPath = new Transaction(document, "New Stairs Path");
    transNewPath.Start();

    // Find StairsPathType
    FilteredElementCollector collector = new FilteredElementCollector(document);
    ICollection<ElementId> stairsPathIds = collector.OfClass(typeof(StairsPathType)).ToElementIds();

    // Find a FloorPlan
    ElementId planViewId = ElementId.InvalidElementId;
    FilteredElementCollector viewCollector = new FilteredElementCollector(document);
    ICollection<ElementId> viewIds = viewCollector.OfClass(typeof(View)).ToElementIds();
    foreach (ElementId viewId in viewIds)
    {
        View view = document.GetElement(viewId) as View;
        if (view.ViewType == ViewType.FloorPlan)
        {
            planViewId = view.Id;
            break;
        }
    }

    LinkElementId stairsLinkId = new LinkElementId(stairs.Id);
    StairsPath.Create(stairs.Document, stairsLinkId, stairsPathIds.First(), planViewId);
    transNewPath.Commit();
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Sub CreateStairsPath(document As Document, stairs As Stairs)
    Dim transNewPath As New Transaction(document, "New Stairs Path")
    transNewPath.Start()

    ' Find StairsPathType
    Dim collector As New FilteredElementCollector(document)
    Dim stairsPathIds As ICollection(Of ElementId) = collector.OfClass(GetType(StairsPathType)).ToElementIds()

    ' Find a FloorPlan
    Dim planViewId As ElementId = ElementId.InvalidElementId
    Dim viewCollector As New FilteredElementCollector(document)
    Dim viewIds As ICollection(Of ElementId) = viewCollector.OfClass(GetType(View)).ToElementIds()
    For Each viewId As ElementId In viewIds
        Dim view As View = TryCast(document.GetElement(viewId), View)
        If view.ViewType = ViewType.FloorPlan Then
            planViewId = view.Id
            Exit For
        End If
    Next

    Dim stairsLinkId As New LinkElementId(stairs.Id)
    StairsPath.Create(stairs.Document, stairsLinkId, stairsPathIds.First(), planViewId)
    transNewPath.Commit()
End Sub
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The stairsId is not a valid stairs. -or- The typeId is not a valid stairs path type. -or- The planViewId is not a valid plan view. -or- The stairsId already has a stairs path. -or- The stairsId is not visible in planViewId. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[StairsPath Class](ed5913d6-1219-9c7c-7e52-317dd58d7cd3.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)