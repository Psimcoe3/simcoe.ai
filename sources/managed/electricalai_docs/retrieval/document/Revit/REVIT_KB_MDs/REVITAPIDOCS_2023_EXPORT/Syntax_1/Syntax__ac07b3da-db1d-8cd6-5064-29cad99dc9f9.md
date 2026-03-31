[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WireLength Property

---



|  |
| --- |
| [FabricWireItem Class](ec68f4e9-ba5a-6036-7d5a-2718689ef95f.htm)   [See Also](#seeAlsoToggle) |

Wire length for this wire item

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public double WireLength { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property WireLength As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double WireLength { 	double get (); 	void set (double value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The given value for length is not a number |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The given value for length must be greater than 0 and no more than 30000 feet. |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | When setting this property: None of the following disciplines is enabled: Structural. |

# See Also

[FabricWireItem Class](ec68f4e9-ba5a-6036-7d5a-2718689ef95f.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)