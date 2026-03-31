[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method

---



|  |
| --- |
| [DividedSurface Class](782e1ac7-4e74-9a32-6b03-0a20f7d55217.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Creates a new instance of a divided surface with a default layout.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public static DividedSurface Create( 	Document document, 	Reference faceReference ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	document As Document, _ 	faceReference As Reference _ ) As DividedSurface ``` |

 

| Visual C++ |
| --- |
| ``` public: static DividedSurface^ Create( 	Document^ document,  	Reference^ faceReference ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

faceReference
:   Type:  [Autodesk.Revit.DB Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)    
     Reference that represents a face.

#### Return Value

The newly created divided surface.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
public void DivideSurface(Document document, Form form)
{
    Autodesk.Revit.ApplicationServices.Application application = document.Application;
    Options opt = application.Create.NewGeometryOptions();
    opt.ComputeReferences = true;

    Autodesk.Revit.DB.GeometryElement geomElem = form.get_Geometry(opt);
    foreach (GeometryObject geomObj in geomElem)
    {
        Solid solid = geomObj as Solid;
        foreach (Face face in solid.Faces)
        {
            if (face.Reference != null)
            {
                DividedSurface ds = DividedSurface.Create(document,face.Reference);
                // create a divided surface with fixed number of U and V grid lines
                SpacingRule srU = ds.USpacingRule;
                srU.SetLayoutFixedNumber(16, SpacingRuleJustification.Center, 0, 0);

                SpacingRule srV = ds.VSpacingRule;
                srV.SetLayoutFixedNumber(24, SpacingRuleJustification.Center, 0, 0);

                break;  // just divide one face of form
            }
        }
    }
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Public Sub DivideSurface(document As Document, form As Form)
    Dim application As Autodesk.Revit.ApplicationServices.Application = document.Application
    Dim opt As Options = application.Create.NewGeometryOptions()
    opt.ComputeReferences = True

    Dim geomElem As Autodesk.Revit.DB.GeometryElement = form.Geometry(opt)
    For Each geomObj As GeometryObject In geomElem
        Dim solid As Solid = TryCast(geomObj, Solid)
        For Each face As Face In solid.Faces
            If face.Reference IsNot Nothing Then
                Dim ds As DividedSurface = DividedSurface.Create(document, face.Reference)
                ' create a divided surface with fixed number of U and V grid lines
                Dim srU As SpacingRule = ds.USpacingRule
                srU.SetLayoutFixedNumber(16, SpacingRuleJustification.Center, 0, 0)

                Dim srV As SpacingRule = ds.VSpacingRule
                srV.SetLayoutFixedNumber(24, SpacingRuleJustification.Center, 0, 0)

                ' just divide one face of form
                Exit For
            End If
        Next
    Next
End Sub
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The document does not allow creation of a divided surface. -or- Reference is unstable import element -or- Reference does not represent a face -or- Reference already hosts a divided surface |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). |
| [Autodesk.Revit.Exceptions ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document has no open transaction. |

# See Also

[DividedSurface Class](782e1ac7-4e74-9a32-6b03-0a20f7d55217.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)