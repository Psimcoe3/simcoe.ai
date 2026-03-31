[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarShapeConstraintChordLength Constructor

---



|  |
| --- |
| [RebarShapeConstraintChordLength Class](b4fee8c1-b79c-e246-9ff5-b1b54fa2056d.htm)   [See Also](#seeAlsoToggle) |

Create a constraint to drive chord length.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public RebarShapeConstraintChordLength( 	ElementId paramId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	paramId As ElementId _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: RebarShapeConstraintChordLength( 	ElementId^ paramId ) ``` |

#### Parameters

paramId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The Id of a Rebar Shape parameter.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | paramId is not a valid Element identifier. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[RebarShapeConstraintChordLength Class](b4fee8c1-b79c-e246-9ff5-b1b54fa2056d.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)