[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NewReferencePoint Method (PointElementReference)

---



|  |
| --- |
| [FamilyItemFactory Class](a7622967-1381-c17f-ed04-1ebe40da0440.htm)   [See Also](#seeAlsoToggle) |

Create a reference point on an existing reference in an Autodesk Revit family document.

**Namespace:**   [Autodesk.Revit.Creation](ded320da-058a-4edd-0418-0582389559a7.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public ReferencePoint NewReferencePoint( 	PointElementReference A_0 ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function NewReferencePoint ( _ 	A_0 As PointElementReference _ ) As ReferencePoint ``` |

 

| Visual C++ |
| --- |
| ``` public: ReferencePoint^ NewReferencePoint( 	PointElementReference^ A_0 ) ``` |

#### Parameters

A\_0
:   Type:  [Autodesk.Revit.DB PointElementReference](f1548185-45ba-c1c6-8bde-4f9bb0669026.htm)

#### Return Value

The newly created ReferencePoint.

# Remarks

The location and coordinate system of the point is determined by the particular PointReference subclass, and the point will remain constrained to that reference.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the argument is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when the family is not a Conceptual Mass Family. |

# See Also

[FamilyItemFactory Class](a7622967-1381-c17f-ed04-1ebe40da0440.htm)

[NewReferencePoint Overload](4c0f388c-4a6a-8803-3be6-07227e4a698a.htm)

[Autodesk.Revit.Creation Namespace](ded320da-058a-4edd-0418-0582389559a7.htm)