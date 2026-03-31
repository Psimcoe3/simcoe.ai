[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### OutOfPlaneBendDiameter Property

---



|  |
| --- |
| [RebarShapeMultiplanarDefinition Class](47a3135c-ce53-c041-f551-0795767eaa41.htm)   [See Also](#seeAlsoToggle) |

Bend diameter to be applied to the connector segments.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public double OutOfPlaneBendDiameter { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property OutOfPlaneBendDiameter As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double OutOfPlaneBendDiameter { 	double get (); 	void set (double value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The given value for outOfPlaneBendDiameter must be greater than 0 and no more than 30000 feet. |

# See Also

[RebarShapeMultiplanarDefinition Class](47a3135c-ce53-c041-f551-0795767eaa41.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)