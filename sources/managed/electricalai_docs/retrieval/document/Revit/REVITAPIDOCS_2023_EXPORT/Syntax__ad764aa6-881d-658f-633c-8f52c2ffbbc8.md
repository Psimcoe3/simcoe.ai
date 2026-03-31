[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidReferenceCurve Method

---



|  |
| --- |
| [DirectShapeType Class](9c7fdd8b-a899-7ba1-2a0f-ecc5e8fe85db.htm)   [See Also](#seeAlsoToggle) |

Validates that the input curve is suitable for creating a direct shape type reference curve. Bounded and unbounded lines are accepted. Other bounded and unbounded curve types with natural bounds are accepted if they are not closed. Unbounded periodic curves are not allowed.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public static bool IsValidReferenceCurve( 	Curve curve ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsValidReferenceCurve ( _ 	curve As Curve _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsValidReferenceCurve( 	Curve^ curve ) ``` |

#### Parameters

curve
:   Type:  [Autodesk.Revit.DB Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)    
     The curve to test.

#### Return Value

True if the input curve point can be used to create a direct shape reference curve, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[DirectShapeType Class](9c7fdd8b-a899-7ba1-2a0f-ecc5e8fe85db.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)