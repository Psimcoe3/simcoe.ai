[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddReferencePlane Method (Plane, BoundingBoxUV, DirectShapeReferenceOptions)

---



|  |
| --- |
| [DirectShapeType Class](9c7fdd8b-a899-7ba1-2a0f-ecc5e8fe85db.htm)   [See Also](#seeAlsoToggle) |

Adds a reference plane to the DirectShapeType. The reference plane can either be bounded or unbounded.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public void AddReferencePlane( 	Plane refPlane, 	BoundingBoxUV boundingBoxUV, 	DirectShapeReferenceOptions options ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub AddReferencePlane ( _ 	refPlane As Plane, _ 	boundingBoxUV As BoundingBoxUV, _ 	options As DirectShapeReferenceOptions _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void AddReferencePlane( 	Plane^ refPlane,  	BoundingBoxUV^ boundingBoxUV,  	DirectShapeReferenceOptions^ options ) ``` |

#### Parameters

refPlane
:   Type:  [Autodesk.Revit.DB Plane](6a6ee978-f114-558d-3c69-00d289aa855f.htm)    
     The geometry of the new reference plane.

boundingBoxUV
:   Type:  [Autodesk.Revit.DB BoundingBoxUV](e38a0145-4267-0b3f-0718-adb14e34c94e.htm)    
     If boundingBoxUV is set, the resulting reference plane that is added to the DirectShapeType will be displayed with those bounds. Note that the specified bounds must not be degenerate. If boundingBoxUV is not set, reasonable bounds are automatically calculated and applied to the input plane. The automatic bounds are based on the host direct shape's geometry.

options
:   Type:  [Autodesk.Revit.DB DirectShapeReferenceOptions](c77da180-10dd-8e8a-d5d4-01cfc06135e5.htm)    
     The options that are used to configure the new reference plane.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | boundingBoxUV cannot be used as a BoundingBoxUV for the reference plane surface. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[DirectShapeType Class](9c7fdd8b-a899-7ba1-2a0f-ecc5e8fe85db.htm)

[AddReferencePlane Overload](af371761-785f-82f8-6c56-5037e961ba01.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)