[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### EnergyModelType Property

---



|  |
| --- |
| [EnergyAnalysisDetailModelOptions Class](18297392-d94a-cdab-feb3-81482771c44d.htm)   [See Also](#seeAlsoToggle) |

It indicates whether the energy model is based on rooms/spaces or building elements.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public EnergyModelType EnergyModelType { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property EnergyModelType As EnergyModelType 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property EnergyModelType EnergyModelType { 	EnergyModelType get (); 	void set (EnergyModelType value); } ``` |

# Remarks

The default value is EnergyModelType::SpatialElement.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[EnergyAnalysisDetailModelOptions Class](18297392-d94a-cdab-feb3-81482771c44d.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)