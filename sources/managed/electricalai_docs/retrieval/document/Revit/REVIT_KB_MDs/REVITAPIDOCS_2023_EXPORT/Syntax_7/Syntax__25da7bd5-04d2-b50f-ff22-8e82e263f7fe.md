[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method (Document, Plane)

---



|  |
| --- |
| [SketchPlane Class](ba104029-d175-7e75-caef-667a4281f4af.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Creates a new sketch plane from a geometric plane.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public static SketchPlane Create( 	Document document, 	Plane plane ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	document As Document, _ 	plane As Plane _ ) As SketchPlane ``` |

 

| Visual C++ |
| --- |
| ``` public: static SketchPlane^ Create( 	Document^ document,  	Plane^ plane ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

plane
:   Type:  [Autodesk.Revit.DB Plane](6a6ee978-f114-558d-3c69-00d289aa855f.htm)    
     The geometry plane where the sketch plane will be created.

#### Return Value

The newly created sketch plane.

# Remarks

There will not be a reference relationship established from the sketch plane to the input face. To create a SketchPlane with a reference to other geometry, use the overload with a Reference input.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
public static SketchPlane CreateSketchPlane(Autodesk.Revit.DB.Document document, Plane plane)
{
    SketchPlane sketchPlane = null;

    // create a sketch plane using Geometry.Plane
    sketchPlane = SketchPlane.Create(document, plane);

    // throw exception if creation failed
    if (null == sketchPlane)
    {
        throw new Exception("Create the sketch plane failed.");
    }

    return sketchPlane;
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Public Shared Function CreateSketchPlane(document As Autodesk.Revit.DB.Document, plane As Plane) As SketchPlane
    Dim sketchPlane__1 As SketchPlane = Nothing

    ' create a sketch plane using Geometry.Plane
    sketchPlane__1 = SketchPlane.Create(document, plane)

    ' throw exception if creation failed
    If sketchPlane__1 Is Nothing Then
        Throw New Exception("Create the sketch plane failed.")
    End If

    Return sketchPlane__1
End Function
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Sketch plane creation is not allowed in this family. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document has no open transaction. |

# See Also

[SketchPlane Class](ba104029-d175-7e75-caef-667a4281f4af.htm)

[Create Overload](51d4403a-b78d-7527-f3bc-463d8044d0d4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)