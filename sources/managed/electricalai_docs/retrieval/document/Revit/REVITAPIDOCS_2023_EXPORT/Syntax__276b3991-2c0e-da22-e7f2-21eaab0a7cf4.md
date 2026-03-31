[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarShapeConstraintAngleFromFixedDir Constructor

---



|  |
| --- |
| [RebarShapeConstraintAngleFromFixedDir Class](11efb7aa-b16b-9c73-bd14-86c3ba4d75c6.htm)   [See Also](#seeAlsoToggle) |

Create an angular constraint.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public RebarShapeConstraintAngleFromFixedDir( 	ElementId paramId, 	int sign, 	UV direction ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	paramId As ElementId, _ 	sign As Integer, _ 	direction As UV _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: RebarShapeConstraintAngleFromFixedDir( 	ElementId^ paramId,  	int sign,  	UV^ direction ) ``` |

#### Parameters

paramId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     A Rebar Shape parameter of type UT\_Angle.

sign
:   Type:  System Int32    
     The sign of the angle relative to the direction.

direction
:   Type:  [Autodesk.Revit.DB UV](1724be37-059b-91ff-aa74-d1508082f76d.htm)    
     A fixed direction in UV-space.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | sign is not 1 or -1. -or- paramId is not a valid Element identifier. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | direction has zero length. |

# See Also

[RebarShapeConstraintAngleFromFixedDir Class](11efb7aa-b16b-9c73-bd14-86c3ba4d75c6.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)