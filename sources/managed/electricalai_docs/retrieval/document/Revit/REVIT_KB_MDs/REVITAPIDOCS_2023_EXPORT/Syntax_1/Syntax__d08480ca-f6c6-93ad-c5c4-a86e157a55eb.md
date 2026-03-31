[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CoverOffset Property

---



|  |
| --- |
| [FabricArea Class](b8e6a637-e069-500d-b7d3-3500e1728681.htm)   [See Also](#seeAlsoToggle) |

The additional cover offset of the fabric distribution.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public double CoverOffset { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property CoverOffset As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double CoverOffset { 	double get (); 	void set (double value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: coverOffset is greater then the host thickness. |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | When setting this property: None of the following disciplines is enabled: Structural. |

# See Also

[FabricArea Class](b8e6a637-e069-500d-b7d3-3500e1728681.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)