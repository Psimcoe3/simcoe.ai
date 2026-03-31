[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddReferenceCurve Method (Curve)

---



|  |
| --- |
| [DirectShapeType Class](9c7fdd8b-a899-7ba1-2a0f-ecc5e8fe85db.htm)   [See Also](#seeAlsoToggle) |

Adds a reference curve to the DirectShapeType.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public void AddReferenceCurve( 	Curve refCurve ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub AddReferenceCurve ( _ 	refCurve As Curve _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void AddReferenceCurve( 	Curve^ refCurve ) ``` |

#### Parameters

refCurve
:   Type:  [Autodesk.Revit.DB Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)    
     The geometry of the new reference curve. First case: The input curve's bounds are set. The resulting reference curve that is added to the DirectShapeType will be displayed with those bounds. Note that the specified bounds must not be degenerate. Second case: The input curve is unbounded. Reasonable bounds are therefore automatically calculated and applied to the input curve. The automatic bounds are based on the host direct shape's geometry. Note that only lines and splines may be unbounded. You must specify valid bounds for all other curve types.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | refCurve cannot be used for creating a reference curve. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[DirectShapeType Class](9c7fdd8b-a899-7ba1-2a0f-ecc5e8fe85db.htm)

[AddReferenceCurve Overload](f795279d-b6d5-8890-9099-e35f67be7c68.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)