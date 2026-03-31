[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Point Property

---



|  |
| --- |
| [BoundaryConditions Class](58a98f0e-e2e5-4c8b-bea1-8228b30f1685.htm)   [See Also](#seeAlsoToggle) |

Returns the position of point boundary conditions.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)

# Syntax

| C# |
| --- |
| ``` public XYZ Point { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Point As XYZ 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property XYZ^ Point { 	XYZ^ get (); } ``` |

# Remarks

Boundary conditions should be BoundaryConditionsType::Point type. Otherwise exception is thrown.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidObjectException](8092dec2-113a-0823-1a09-a46c11f99fea.htm) | Thrown when BoundaryConditions is not a BoundaryConditionsType::Point type. |

# See Also

[BoundaryConditions Class](58a98f0e-e2e5-4c8b-bea1-8228b30f1685.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)