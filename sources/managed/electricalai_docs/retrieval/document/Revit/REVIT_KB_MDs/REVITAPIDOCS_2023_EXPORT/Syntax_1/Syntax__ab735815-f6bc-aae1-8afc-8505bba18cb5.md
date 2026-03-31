[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateByNormalAndOrigin Method

---



|  |
| --- |
| [Plane Class](6a6ee978-f114-558d-3c69-00d289aa855f.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Constructs a Plane object from a normal and an origin represented as XYZ objects. Follows the standard conventions for a planar surface. The constructed Plane object will pass through origin and be perpendicular to normal. The X and Y axes of the plane will be defined arbitrarily.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public static Plane CreateByNormalAndOrigin( 	XYZ normal, 	XYZ origin ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateByNormalAndOrigin ( _ 	normal As XYZ, _ 	origin As XYZ _ ) As Plane ``` |

 

| Visual C++ |
| --- |
| ``` public: static Plane^ CreateByNormalAndOrigin( 	XYZ^ normal,  	XYZ^ origin ) ``` |

#### Parameters

normal
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     Plane normal. Expected to be a valid non-zero length vector. Doesn't need to be a unit vector.

origin
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     Plane origin. Expected to lie within the Revit design limits  [IsWithinLengthLimits(XYZ)](ac2171af-4250-8a30-faa7-4d7030d29a03.htm)  .

# Remarks

This function does not guarantee a specific parameterization of the created Plane. Use Plane.Create(Frame) to enforce a specific parameterization of the created Plane object.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
 // Create a geometry plane in Revit application
XYZ normal = XYZ.BasisZ;    // use basis of the z-axis (0,0,1) for normal vector 
XYZ origin = XYZ.Zero;  // origin is (0,0,0)  
Plane geomPlane = Plane.CreateByNormalAndOrigin(normal, origin);
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
   ' Create a geometry plane in Revit application
   Dim normal As XYZ = XYZ.BasisZ
   ' use basis of the z-axis (0,0,1) for normal vector 
   Dim origin As XYZ = XYZ.Zero
   ' origin is (0,0,0)  
Dim geomPlane As Plane = Plane.CreateByNormalAndOrigin(normal, origin)
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The input point lies outside of Revit design limits. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | normal has zero length. |

# See Also

[Plane Class](6a6ee978-f114-558d-3c69-00d289aa855f.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)