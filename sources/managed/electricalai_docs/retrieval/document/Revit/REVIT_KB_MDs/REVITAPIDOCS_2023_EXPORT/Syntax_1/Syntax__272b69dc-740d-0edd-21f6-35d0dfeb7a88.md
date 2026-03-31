[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LevelOffset Property

---



|  |
| --- |
| [GenericZone Class](100b5109-f779-8cf8-81d1-cb6a5c0f4fa1.htm)   [See Also](#seeAlsoToggle) |

The offset distance from this zone to the associated level.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2021.1

# Syntax

| C# |
| --- |
| ``` public double LevelOffset { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property LevelOffset As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double LevelOffset { 	double get (); 	void set (double value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The given value for offset must be no more than 30000 feet in absolute value. |

# See Also

[GenericZone Class](100b5109-f779-8cf8-81d1-cb6a5c0f4fa1.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)