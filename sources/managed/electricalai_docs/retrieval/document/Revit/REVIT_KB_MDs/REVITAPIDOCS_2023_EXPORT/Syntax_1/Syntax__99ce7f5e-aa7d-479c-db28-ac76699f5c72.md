[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarShapeConstraintProjectedSegmentLength Constructor

---



|  |
| --- |
| [RebarShapeConstraintProjectedSegmentLength Class](a41486b4-25c4-c955-f1ab-c585ffb92bd2.htm)   [See Also](#seeAlsoToggle) |

Constructs a new instance of a RebarConstraintProjectEdgedLength object using a shape parameter, direction, and reference types.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public RebarShapeConstraintProjectedSegmentLength( 	ElementId paramId, 	UV direction, 	int tripleProductSign, 	RebarShapeSegmentEndReferenceType refType0, 	RebarShapeSegmentEndReferenceType refType1 ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	paramId As ElementId, _ 	direction As UV, _ 	tripleProductSign As Integer, _ 	refType0 As RebarShapeSegmentEndReferenceType, _ 	refType1 As RebarShapeSegmentEndReferenceType _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: RebarShapeConstraintProjectedSegmentLength( 	ElementId^ paramId,  	UV^ direction,  	int tripleProductSign,  	RebarShapeSegmentEndReferenceType refType0,  	RebarShapeSegmentEndReferenceType refType1 ) ``` |

#### Parameters

paramId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The Id of a Rebar Shape parameter.

direction
:   Type:  [Autodesk.Revit.DB UV](1724be37-059b-91ff-aa74-d1508082f76d.htm)    
     A vector specifying the direction of the constraint. The direction is fixed, and the shape is always constructed so that the segment's direction has a positive dot product with this vector.

tripleProductSign
:   Type:  System Int32    
     Sign of the z-coordinate of the cross product of the "direction" argument with the segment vector. In other words, 1 if the segment direction is to be on the left of the constraint direction, or -1 if the segment direction is to be on the right.

refType0
:   Type:  [Autodesk.Revit.DB.Structure RebarShapeSegmentEndReferenceType](92c3fafa-996d-cca9-cc7e-a73d4c94ae57.htm)    
     Choose between two possibilities for the first reference of the length constraint.

refType1
:   Type:  [Autodesk.Revit.DB.Structure RebarShapeSegmentEndReferenceType](92c3fafa-996d-cca9-cc7e-a73d4c94ae57.htm)    
     Choose between two possibilities for the second reference of the length constraint.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | paramId is not a valid Element identifier. -or- tripleProductSign is not 1 or -1. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | direction has zero length. -or- A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[RebarShapeConstraintProjectedSegmentLength Class](a41486b4-25c4-c955-f1ab-c585ffb92bd2.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)