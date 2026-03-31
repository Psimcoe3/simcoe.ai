[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BuildingOperatingSchedule Property

---



|  |
| --- |
| [EnergyDataSettings Class](63628109-daa0-e5b2-3dfd-153179e54816.htm)   [See Also](#seeAlsoToggle) |

The operating schedule of the building used for conceptual model energy calculations.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public gbXMLBuildingOperatingSchedule BuildingOperatingSchedule { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property BuildingOperatingSchedule As gbXMLBuildingOperatingSchedule 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property gbXMLBuildingOperatingSchedule BuildingOperatingSchedule { 	gbXMLBuildingOperatingSchedule get (); 	void set (gbXMLBuildingOperatingSchedule value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The building operating schedule does not fall within an appropriate range. |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[EnergyDataSettings Class](63628109-daa0-e5b2-3dfd-153179e54816.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)