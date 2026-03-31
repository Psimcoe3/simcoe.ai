[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method (Document, ElementId, ElementId, ElementId, XYZ, XYZ, IList(XYZ))

---



|  |
| --- |
| [FlexDuct Class](39e3bd3a-8304-7785-dd10-4043aa0d7da4.htm)   [See Also](#seeAlsoToggle) |

Creates a new flexible duct into the document, using a point array and flexible duct type.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public static FlexDuct Create( 	Document document, 	ElementId systemTypeId, 	ElementId ductTypeId, 	ElementId levelId, 	XYZ startTangent, 	XYZ endTangent, 	IList<XYZ> points ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	document As Document, _ 	systemTypeId As ElementId, _ 	ductTypeId As ElementId, _ 	levelId As ElementId, _ 	startTangent As XYZ, _ 	endTangent As XYZ, _ 	points As IList(Of XYZ) _ ) As FlexDuct ``` |

 

| Visual C++ |
| --- |
| ``` public: static FlexDuct^ Create( 	Document^ document,  	ElementId^ systemTypeId,  	ElementId^ ductTypeId,  	ElementId^ levelId,  	XYZ^ startTangent,  	XYZ^ endTangent,  	IList<XYZ^>^ points ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

systemTypeId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of the HVAC system type.

ductTypeId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of the flexible duct.

levelId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The level id for the flexible duct.

startTangent
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The tangent vector at the start of the curve. The invalid or zero vector is ignored.

endTangent
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The tangent vector at the end of the curve. The invalid or zero vector is ignored.

points
:   Type:  System.Collections.Generic IList   [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The point array indicating the path of the flexible duct, including the end point.

#### Return Value

If creation was successful then a new flexible duct is returned, otherwise an exception with failure information will be thrown.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The systemTypeId is not valid HVAC system type. -or- The type ductTypeId is not valid flexible duct type. -or- The ElementId levelId is not a Level. -or- The valid number of points is less than two. In order to create a flex curve, at least two points are required. Note the duplicate points don't take into account. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Mechanical Electrical Piping. |

# See Also

[FlexDuct Class](39e3bd3a-8304-7785-dd10-4043aa0d7da4.htm)

[Create Overload](4bea1e5e-5073-7faa-a787-837bb0dca901.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)