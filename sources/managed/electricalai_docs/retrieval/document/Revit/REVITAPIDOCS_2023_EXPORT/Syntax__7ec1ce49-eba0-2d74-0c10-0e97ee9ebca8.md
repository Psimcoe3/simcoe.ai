[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NewRevolveForms Method

---



|  |
| --- |
| [FamilyItemFactory Class](a7622967-1381-c17f-ed04-1ebe40da0440.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Create new Form elements by revolve operation, and add them into the Autodesk Revit family document.

**Namespace:**   [Autodesk.Revit.Creation](ded320da-058a-4edd-0418-0582389559a7.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)

# Syntax

| C# |
| --- |
| ``` public FormArray NewRevolveForms( 	bool isSolid, 	ReferenceArray profile, 	Reference axis, 	double startAngle, 	double endAngle ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function NewRevolveForms ( _ 	isSolid As Boolean, _ 	profile As ReferenceArray, _ 	axis As Reference, _ 	startAngle As Double, _ 	endAngle As Double _ ) As FormArray ``` |

 

| Visual C++ |
| --- |
| ``` public: FormArray^ NewRevolveForms( 	bool isSolid,  	ReferenceArray^ profile,  	Reference^ axis,  	double startAngle,  	double endAngle ) ``` |

#### Parameters

isSolid
:   Type:  [System Boolean](http://msdn2.microsoft.com/en-us/library/a28wyd50)    
     Indicates if the Form is Solid or Void.

profile
:   Type:  [Autodesk.Revit.DB ReferenceArray](bc9192b5-6666-a8de-0128-87dae479fd6a.htm)    
     The profile of the newly created revolution. It should consist of only one curve loop. The profile must be in the same plane as the axis.

axis
:   Type:  [Autodesk.Revit.DB Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)    
     The axis of revolution. The axis is a line that must lie in the same plane as the curves in the profile.

startAngle
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The start angle of Revolution in radians.

endAngle
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The end angle of Revolution in radians.

#### Return Value

If creation was successful new forms are returned.

# Remarks

Typically this operation produces only a single form, but some combinations of arguments will create multiple forms from a single profile.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
private FormArray CreateRevolveForm(Document document)
{
    FormArray revolveForms = null;

    // Create one profile
    ReferenceArray ref_ar = new ReferenceArray();

    XYZ ptA = new XYZ(0, 0, 10);
    XYZ ptB = new XYZ(100, 0, 10);
    Line line = Line.CreateBound(ptA, ptB);
    ModelCurve modelcurve = MakeLine(document, ptA, ptB);
    ref_ar.Append(modelcurve.GeometryCurve.Reference);

    ptA = new XYZ(100, 0, 10);
    ptB = new XYZ(100, 100, 10);
    modelcurve = MakeLine(document, ptA, ptB);
    ref_ar.Append(modelcurve.GeometryCurve.Reference);

    ptA = new XYZ(100, 100, 10);
    ptB = new XYZ(0, 0, 10);
    modelcurve = MakeLine(document, ptA, ptB);
    ref_ar.Append(modelcurve.GeometryCurve.Reference);

    // Create axis for revolve form
    ptA = new XYZ(-5, 0, 10);
    ptB = new XYZ(-5, 10, 10);
    ModelCurve axis = MakeLine(document, ptA, ptB);

    // make axis a Reference Line
    axis.ChangeToReferenceLine();

    // Typically this operation produces only a single form, 
    // but some combinations of arguments will create multiple froms from a single profile.
    revolveForms = document.FamilyCreate.NewRevolveForms(true, ref_ar, axis.GeometryCurve.Reference, 0, Math.PI / 4);

    return revolveForms;
}

public ModelCurve MakeLine(Document doc, XYZ ptA, XYZ ptB)
{
    Autodesk.Revit.ApplicationServices.Application app = doc.Application;
    // Create plane by the points
    Line line = Line.CreateBound(ptA, ptB);
    XYZ norm = ptA.CrossProduct(ptB);
    if (norm.IsZeroLength()) norm = XYZ.BasisZ;
    Plane plane = Plane.CreateByNormalAndOrigin(norm, ptB);
    SketchPlane skplane = SketchPlane.Create(doc, plane);
    // Create line here
    ModelCurve modelcurve = doc.FamilyCreate.NewModelCurve(line, skplane);
    return modelcurve;
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Function CreateRevolveForm(document As Document) As FormArray
    Dim revolveForms As FormArray = Nothing

    ' Create one profile
    Dim ref_ar As New ReferenceArray()

    Dim ptA As New XYZ(0, 0, 10)
    Dim ptB As New XYZ(100, 0, 10)
    Dim line__1 As Line = Line.CreateBound(ptA, ptB)
    Dim modelcurve As ModelCurve = MakeLine(document, ptA, ptB)
    ref_ar.Append(modelcurve.GeometryCurve.Reference)

    ptA = New XYZ(100, 0, 10)
    ptB = New XYZ(100, 100, 10)
    modelcurve = MakeLine(document, ptA, ptB)
    ref_ar.Append(modelcurve.GeometryCurve.Reference)

    ptA = New XYZ(100, 100, 10)
    ptB = New XYZ(0, 0, 10)
    modelcurve = MakeLine(document, ptA, ptB)
    ref_ar.Append(modelcurve.GeometryCurve.Reference)

    ' Create axis for revolve form
    ptA = New XYZ(-5, 0, 10)
    ptB = New XYZ(-5, 10, 10)
    Dim axis As ModelCurve = MakeLine(document, ptA, ptB)

    ' make axis a Reference Line
    axis.ChangeToReferenceLine()

    ' Typically this operation produces only a single form, 
    ' but some combinations of arguments will create multiple froms from a single profile.
    revolveForms = document.FamilyCreate.NewRevolveForms(True, ref_ar, axis.GeometryCurve.Reference, 0, Math.PI / 4)

    Return revolveForms
End Function

Public Function MakeLine(doc As Document, ptA As XYZ, ptB As XYZ) As ModelCurve
    Dim app As Autodesk.Revit.ApplicationServices.Application = doc.Application
    ' Create plane by the points
    Dim line__1 As Line = Line.CreateBound(ptA, ptB)
    Dim norm As XYZ = ptA.CrossProduct(ptB)
    If norm.IsZeroLength() Then
        norm = XYZ.BasisZ
    End If
 Dim plane As Plane = plane.CreateByNormalAndOrigin(norm, ptB)
    Dim skplane As SketchPlane = SketchPlane.Create(doc, plane)
    ' Create line here
    Dim modelcurve As ModelCurve = doc.FamilyCreate.NewModelCurve(line__1, skplane)
    Return modelcurve
End Function
```

# See Also

[FamilyItemFactory Class](a7622967-1381-c17f-ed04-1ebe40da0440.htm)

[Autodesk.Revit.Creation Namespace](ded320da-058a-4edd-0418-0582389559a7.htm)