[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetTargetHostFaceAndTransform Method

---



|  |
| --- |
| [RebarConstraint Class](748823c8-f059-68c1-d7b5-7cfaba93a445.htm)   [See Also](#seeAlsoToggle) |

Returns the face to which the RebarConstraint is attached associated to the given target index. The RebarConstraintType of the RebarConstraint must be 'FixedDistanceToHostFace' or 'ToCover.'

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public Face GetTargetHostFaceAndTransform( 	int targetIndex, 	Transform faceTransform ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetTargetHostFaceAndTransform ( _ 	targetIndex As Integer, _ 	faceTransform As Transform _ ) As Face ``` |

 

| Visual C++ |
| --- |
| ``` public: Face^ GetTargetHostFaceAndTransform( 	int targetIndex,  	Transform^ faceTransform ) ``` |

#### Parameters

targetIndex
:   Type:  System Int32    
     The index of the target. Should be between 0 and NumberOfTargets().

faceTransform
:   Type:  [Autodesk.Revit.DB Transform](58dd01c8-b3fc-7142-e4f3-c524079a282d.htm)    
     Returns the transform that is associated to the face's element geometry.

#### Return Value

Requested Face.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | targetIndex is out of range. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | RebarConstraint is no longer valid. -or- The RebarConstraint is not of RebarConstraintType 'FixedDistanceToHostFace' or 'ToCover.' |

# See Also

[RebarConstraint Class](748823c8-f059-68c1-d7b5-7cfaba93a445.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)