[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PlanarFace Class

---



|  |
| --- |
| [Members](a97f6d34-2b01-6e3c-ec17-89743f4aceca.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

A bounded face of a 3d solid or open shell.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)

# Syntax

| C# |
| --- |
| ``` public class PlanarFace : Face ``` |

 

| Visual Basic |
| --- |
| ``` Public Class PlanarFace _ 	Inherits Face ``` |

 

| Visual C++ |
| --- |
| ``` public ref class PlanarFace : public Face ``` |

# Remarks

Planar faces are defined by planes bounded by edge loops. The planes provide natural UV parameterization to the faces. S(u, v) = Origin + u\*Vector[0] + v\*Vector[1]

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
private void GetPlanarFaceInfo(Face face)
{
    PlanarFace planarFace = face as PlanarFace;
    if (null != planarFace)
    {
       XYZ origin = planarFace.Origin;
        XYZ normal = planarFace.FaceNormal;
        XYZ vector = planarFace.XVector;
    }
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Sub GetPlanarFaceInfo(face As Face)
   Dim planarFace As PlanarFace = TryCast(face, PlanarFace)
   If planarFace IsNot Nothing Then
      Dim origin As XYZ = planarFace.Origin
      Dim normal As XYZ = planarFace.FaceNormal
      Dim vector As XYZ = planarFace.XVector
   End If
End Sub
```

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm)    
  [Autodesk.Revit.DB GeometryObject](e0f15010-0e19-6216-e2f0-ab7978145daa.htm)    
  [Autodesk.Revit.DB Face](e32b3b1f-66fc-57cb-6e1c-aa81d1bf3e63.htm)    
  Autodesk.Revit.DB PlanarFace

# See Also

[PlanarFace Members](a97f6d34-2b01-6e3c-ec17-89743f4aceca.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)