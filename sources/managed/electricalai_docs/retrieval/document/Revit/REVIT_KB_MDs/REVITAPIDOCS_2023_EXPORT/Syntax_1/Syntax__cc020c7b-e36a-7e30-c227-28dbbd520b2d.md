[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HermiteFace Class

---



|  |
| --- |
| [Members](4542a8cd-be81-9bf3-3892-aba1e0aa0106.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

A cubic hermite spline face of a 3d solid or open shell.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)

# Syntax

| C# |
| --- |
| ``` public class HermiteFace : Face ``` |

 

| Visual Basic |
| --- |
| ``` Public Class HermiteFace _ 	Inherits Face ``` |

 

| Visual C++ |
| --- |
| ``` public ref class HermiteFace : public Face ``` |

# Remarks

Hermite faces are defined by cubic hermite spline surfaces bounded by edge loops. The surfaces provide natural UV parameterization to the faces.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
private void GetHermiteFaceInfo(Face face)
{
    HermiteFace hermiteFace = face as HermiteFace;
    if (null != hermiteFace)
    {
        IList<XYZ> points = hermiteFace.Points;
        IList<XYZ> derivs = hermiteFace.MixedDerivs;
        DoubleArray faceParams = hermiteFace.get_Params(0);
        IList<XYZ> tangents = hermiteFace.get_Tangents(0);
    }
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Sub GetHermiteFaceInfo(face As Face)
    Dim hermiteFace As HermiteFace = TryCast(face, HermiteFace)
    If hermiteFace IsNot Nothing Then
        Dim points As IList(Of XYZ) = hermiteFace.Points
        Dim derivs As IList(Of XYZ) = hermiteFace.MixedDerivs
        Dim faceParams As DoubleArray = hermiteFace.Params(0)
        Dim tangents As IList(Of XYZ) = hermiteFace.Tangents(0)
    End If
End Sub
```

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm)    
  [Autodesk.Revit.DB GeometryObject](e0f15010-0e19-6216-e2f0-ab7978145daa.htm)    
  [Autodesk.Revit.DB Face](e32b3b1f-66fc-57cb-6e1c-aa81d1bf3e63.htm)    
  Autodesk.Revit.DB HermiteFace

# See Also

[HermiteFace Members](4542a8cd-be81-9bf3-3892-aba1e0aa0106.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)