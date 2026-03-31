[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AppendShape Method (IList(GeometryObject))

---



|  |
| --- |
| [DirectShapeType Class](9c7fdd8b-a899-7ba1-2a0f-ecc5e8fe85db.htm)   [See Also](#seeAlsoToggle) |

Appends the collection of GeometryObjects into the model shape representation stored in this DirectShape.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public void AppendShape( 	IList<GeometryObject> pGeomArr ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub AppendShape ( _ 	pGeomArr As IList(Of GeometryObject) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void AppendShape( 	IList<GeometryObject^>^ pGeomArr ) ``` |

#### Parameters

pGeomArr
:   Type:  System.Collections.Generic IList   [GeometryObject](e0f15010-0e19-6216-e2f0-ab7978145daa.htm)    
     Shape expressed as a collection of GeometryObjects. The supported types of GeometryObjects are: Solid, Mesh, GeometryInstance, Point, Curve and PolyLine.

# Remarks

The existing shape will not be cleared by this function, and intersecting or overlapped geometry will not be joined with the appended geometry. It is up to the caller to ensure that the combination of geometry will have the correct appearance in Revit.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | At least one member of pGeomArr does not satisfy DirectShapeType validation criteria. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[DirectShapeType Class](9c7fdd8b-a899-7ba1-2a0f-ecc5e8fe85db.htm)

[AppendShape Overload](d2655b07-cda2-51c9-071c-c0db4843a37f.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)