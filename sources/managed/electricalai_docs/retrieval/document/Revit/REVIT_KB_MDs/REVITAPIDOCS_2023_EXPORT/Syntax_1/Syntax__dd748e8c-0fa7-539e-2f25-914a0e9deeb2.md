[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarShapeConstraintCircumference Constructor

---



|  |
| --- |
| [RebarShapeConstraintCircumference Class](1834e2d5-cc02-e1f3-3e17-8058593ff6f7.htm)   [See Also](#seeAlsoToggle) |

Create a circumference constraint.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public RebarShapeConstraintCircumference( 	ElementId paramId, 	RebarShapeArcReferenceType refType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	paramId As ElementId, _ 	refType As RebarShapeArcReferenceType _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: RebarShapeConstraintCircumference( 	ElementId^ paramId,  	RebarShapeArcReferenceType refType ) ``` |

#### Parameters

paramId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The Id of a Rebar Shape parameter.

refType
:   Type:  [Autodesk.Revit.DB.Structure RebarShapeArcReferenceType](0552910e-83f5-70bb-4b87-14ce00d10bdb.htm)    
     A choice of rule for measuring the circumference.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | paramId is not a valid Element identifier. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[RebarShapeConstraintCircumference Class](1834e2d5-cc02-e1f3-3e17-8058593ff6f7.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)