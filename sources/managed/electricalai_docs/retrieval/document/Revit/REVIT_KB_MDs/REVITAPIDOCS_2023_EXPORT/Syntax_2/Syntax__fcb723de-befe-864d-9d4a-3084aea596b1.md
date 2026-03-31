[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateMultiPlaneFilter Method (IList(Plane))

---



|  |
| --- |
| [PointCloudFilterFactory Class](fcbc90c3-0a9d-7522-e483-cad73468d698.htm)   [See Also](#seeAlsoToggle) |

Creates a new point cloud filter based upon planar boundaries.

**Namespace:**   [Autodesk.Revit.DB.PointClouds](5974062a-47d4-c7bb-16f2-d5dd193bd170.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static PointCloudFilter CreateMultiPlaneFilter( 	IList<Plane> planes ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateMultiPlaneFilter ( _ 	planes As IList(Of Plane) _ ) As PointCloudFilter ``` |

 

| Visual C++ |
| --- |
| ``` public: static PointCloudFilter^ CreateMultiPlaneFilter( 	IList<Plane^>^ planes ) ``` |

#### Parameters

planes
:   Type:  System.Collections.Generic IList   [Plane](6a6ee978-f114-558d-3c69-00d289aa855f.htm)    
     All planes used for filtering; positive direction of the normal should point inside the volume of interest. Only points on the "positive" side of all planes will pass the filter.

#### Return Value

Filter object; can be used to get representative set of cloud points passing through the filter.

# Remarks

The filter will check whether a point is located on the "positive" side of each plane, as indicated by the positive direction of the plane normal. Therefore, such filter implicitly defines a volume, which is the intersection of the positive half-spaces corresponding to all the planes. This volume does not have to be closed, but it will always be convex.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[PointCloudFilterFactory Class](fcbc90c3-0a9d-7522-e483-cad73468d698.htm)

[CreateMultiPlaneFilter Overload](69cc8914-6168-abf1-1e37-d2bc48a5ba18.htm)

[Autodesk.Revit.DB.PointClouds Namespace](5974062a-47d4-c7bb-16f2-d5dd193bd170.htm)