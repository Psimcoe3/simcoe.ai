[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsBindingHandleWithTarget Method

---



|  |
| --- |
| [RebarConstraint Class](748823c8-f059-68c1-d7b5-7cfaba93a445.htm)   [See Also](#seeAlsoToggle) |

Gets the relationship between two RebarConstrainedHandles.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2020.1

# Syntax

| C# |
| --- |
| ``` public bool IsBindingHandleWithTarget() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsBindingHandleWithTarget As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsBindingHandleWithTarget() ``` |

#### Return Value

Returns False if only the constrained RebarConstrainedHandle follows the target. Returns True if the constrained RebarConstrainedHandle and the target bar handle are bound and move together.

# Remarks

Throws exception for any type of constraint other than 'ToOtherRebar' or if the RebarTargetConstraintType of the constraint is 'HookBend' or 'BarBend'. Will also throw if the target Rebar has the 'Number with Spacing' layout rule and the RebarTargetConstraintType of the constraint is 'OutOfPlaneExtent'.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | RebarConstraint is no longer valid. -or- The RebarConstraint is not of RebarConstraintType 'ToOtherRebar.' -or- The RebarTargetConstraintType is 'HookBend' or 'BarBend'. -or- The RebarTargetConstraintType is 'OutOfPlaneExtent' and the rebar target layout is 'Number with Spacing'. |

# See Also

[RebarConstraint Class](748823c8-f059-68c1-d7b5-7cfaba93a445.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)