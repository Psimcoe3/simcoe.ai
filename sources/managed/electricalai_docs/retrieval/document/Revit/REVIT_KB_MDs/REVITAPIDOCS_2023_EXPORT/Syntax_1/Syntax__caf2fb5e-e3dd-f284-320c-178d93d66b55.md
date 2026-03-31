[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetLoops Method

---



|  |
| --- |
| [BoundaryConditions Class](58a98f0e-e2e5-4c8b-bea1-8228b30f1685.htm)   [See Also](#seeAlsoToggle) |

Returns curve loops that define geometry of the area boundary conditions.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public IList<CurveLoop> GetLoops() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetLoops As IList(Of CurveLoop) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<CurveLoop^>^ GetLoops() ``` |

#### Return Value

The curve loop collection.

# Remarks

Boundary conditions should be BoundaryConditionsType::Area type. Otherwise exception is thrown.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidObjectException](8092dec2-113a-0823-1a09-a46c11f99fea.htm) | Thrown when BoundaryConditions is not a BoundaryConditionsType::Area type. |

# See Also

[BoundaryConditions Class](58a98f0e-e2e5-4c8b-bea1-8228b30f1685.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)