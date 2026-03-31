[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetConstraints Method

---



|  |
| --- |
| [RebarShapeDefinitionByArc Class](a92742a5-9781-3691-ec78-5b318fbf5ad3.htm)   [See Also](#seeAlsoToggle) |

Assign a new list of constraints to this definition.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public void SetConstraints( 	IList<RebarShapeConstraint> constraints ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetConstraints ( _ 	constraints As IList(Of RebarShapeConstraint) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetConstraints( 	IList<RebarShapeConstraint^>^ constraints ) ``` |

#### Parameters

constraints
:   Type:  System.Collections.Generic IList   [RebarShapeConstraint](21c642f3-7aae-759b-4aac-ff4e2dd77d57.htm)    
     A new list of constraints.

# Remarks

Any existing constraints are discarded. The new constraints replace them. Any parameters driving the constraints must already be added with AddParameter().

If the Type is Arc or LappedCircle, the allowable constraint types are:

* RebarShapeConstraintArcLength
* RebarShapeConstraintRadius
* RebarShapeConstraintDiameter
* RebarShapeConstraintCircumference
* RebarShapeConstraintSagittaLength
* RebarShapeConstraintChordLength

At least two independent constraints must be specified. Overconstraining is supported.

If the Type is Spiral, the allowable constraints are:

* RebarShapeConstraintRadius
* RebarShapeConstraintDiameter
* RebarShapeConstraintCircumference

At least one constraint must be specified.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | One or more of the constraints is of a type not supported for this definition. -or- One or more of the constraints refers to a parameter that has not been added yet. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[RebarShapeDefinitionByArc Class](a92742a5-9781-3691-ec78-5b318fbf5ad3.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)