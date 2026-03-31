[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetTargetHostFaceReference Method

---



|  |
| --- |
| [RebarConstraint Class](748823c8-f059-68c1-d7b5-7cfaba93a445.htm)   [See Also](#seeAlsoToggle) |

Returns a reference to the host Element face to which the RebarConstraint is attached. The RebarConstraintType of the RebarConstraint must be 'FixedDistanceToHostFace' or 'ToCover.' Will throw exception if it's a multi target constraint.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public Reference GetTargetHostFaceReference() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetTargetHostFaceReference As Reference ``` |

 

| Visual C++ |
| --- |
| ``` public: Reference^ GetTargetHostFaceReference() ``` |

#### Return Value

Requested reference.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | RebarConstraint is no longer valid. -or- The RebarConstraint is not of RebarConstraintType 'FixedDistanceToHostFace' or 'ToCover.' -or- Multi target constraint. Consider using the indexed version of the method. |

# See Also

[RebarConstraint Class](748823c8-f059-68c1-d7b5-7cfaba93a445.htm)

[GetTargetHostFaceReference Overload](ae76f8f5-0c2f-c059-fc30-5f112355affc.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)