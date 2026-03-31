[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateDetail Method

---



|  |
| --- |
| [ViewSection Class](fcc75682-bd99-a97d-5a4d-0f8eb9e92ab5.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Returns a new detail ViewSection.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static ViewSection CreateDetail( 	Document document, 	ElementId viewFamilyTypeId, 	BoundingBoxXYZ sectionBox ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateDetail ( _ 	document As Document, _ 	viewFamilyTypeId As ElementId, _ 	sectionBox As BoundingBoxXYZ _ ) As ViewSection ``` |

 

| Visual C++ |
| --- |
| ``` public: static ViewSection^ CreateDetail( 	Document^ document,  	ElementId^ viewFamilyTypeId,  	BoundingBoxXYZ^ sectionBox ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document to which the new detail ViewSection will be added.

viewFamilyTypeId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of the ViewFamilyType which will be used by the new detail ViewSection. The type needs to be a Detail ViewFamily.

sectionBox
:   Type:  [Autodesk.Revit.DB BoundingBoxXYZ](3c452286-57b1-40e2-2795-c90bff1fcec2.htm)    
     The BoundingBoxXYZ which specifies the new ViewSection's view direction and extents.

#### Return Value

The new detail ViewSection.

# Remarks

Create a detail ViewSection whose view volume corresponds geometrically with the specified sectionBox. The view direction of the resulting section will be sectionBox.Transform.BasisZ and the up direction will be sectionBox.Transform.BasisY. The right hand direction will be computed so that (right, up, view direction) form a left handed coordinate system. The resulting view will be cropped, and far clipping will be active. The crop region will correspond to the projections of BoundingBoxXYZ.Min and BoundingBoxXYZ.Max onto the view's cut plane. The far clip distance will be equal to the difference of the z-coordinates of BoundingBoxXYZ.Min and BoundingBoxXYZ.Max. The new detail ViewSection will receive a unique view name.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
// Get a BoundingBoxXYZ instance from Revit
BoundingBoxXYZ box = document.ActiveView.CropBox;
if (null == box)
{
    throw new Exception("No BoundingBoxXYZ instance found.");
}

// Create a new view section.
ElementId DetailViewId = ElementId.InvalidElementId;
IList<Element> elems = new FilteredElementCollector(document).OfClass(typeof(ViewFamilyType)).ToElements();
foreach (Element e in elems)
{
    ViewFamilyType v = e as ViewFamilyType;

    if (v != null && v.ViewFamily == ViewFamily.Detail)
    {
        DetailViewId = e.Id;
        break;
    }
}
ViewSection viewSection = ViewSection.CreateDetail(document, DetailViewId, box);
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
' Get a BoundingBoxXYZ instance from Revit
Dim box As BoundingBoxXYZ = document.ActiveView.CropBox
If box Is Nothing Then
    Throw New Exception("No BoundingBoxXYZ instance found.")
End If

' Create a new view section.
Dim DetailViewId As ElementId = ElementId.InvalidElementId
Dim elems As IList(Of Element) = New FilteredElementCollector(document).OfClass(GetType(ViewFamilyType)).ToElements()
For Each e As Element In elems
    Dim v As ViewFamilyType = TryCast(e, ViewFamilyType)

    If v IsNot Nothing AndAlso v.ViewFamily = ViewFamily.Detail Then
        DetailViewId = e.Id
        Exit For
    End If
Next
Dim viewSection__1 As ViewSection = ViewSection.CreateDetail(document, DetailViewId, box)
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The ViewFamilyType must be a Detail ViewFamily. -or- The BoundingBoxXYZ is not appropriate for detail views. The basis vectors of must be unit length and orthonormal. The near and far bound offsets cannot be reversed or too close to each other. MinEnabled and MaxEnabled must be set to true for all three directions. -or- Detail section view creation is not allowed in this family. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document has no open transaction. |

# See Also

[ViewSection Class](fcc75682-bd99-a97d-5a4d-0f8eb9e92ab5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)