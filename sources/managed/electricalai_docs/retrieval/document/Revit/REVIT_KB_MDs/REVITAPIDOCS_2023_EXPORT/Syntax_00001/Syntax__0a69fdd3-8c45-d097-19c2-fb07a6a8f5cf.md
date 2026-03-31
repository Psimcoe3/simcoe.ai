[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BentFabricBendDirection Property

---



|  |
| --- |
| [FabricSheet Class](1f420619-ab30-942a-e5b6-028b7ff3889f.htm)   [See Also](#seeAlsoToggle) |

Specifies which wire direction of the fabric sheet is bent.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public BentFabricBendDirection BentFabricBendDirection { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property BentFabricBendDirection As BentFabricBendDirection 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property BentFabricBendDirection BentFabricBendDirection { 	BentFabricBendDirection get (); 	void set (BentFabricBendDirection value); } ``` |

# Remarks

This parameter applies only to bent fabric sheets.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: the data-setting method is not applicable to fabric sheets that are flat |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | When setting this property: None of the following disciplines is enabled: Structural. |
| [Autodesk.Revit.Exceptions InvalidObjectException](8092dec2-113a-0823-1a09-a46c11f99fea.htm) | When setting this property: The data-setting method is not applicable to fabric sheets that are flat. |

# See Also

[FabricSheet Class](1f420619-ab30-942a-e5b6-028b7ff3889f.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)