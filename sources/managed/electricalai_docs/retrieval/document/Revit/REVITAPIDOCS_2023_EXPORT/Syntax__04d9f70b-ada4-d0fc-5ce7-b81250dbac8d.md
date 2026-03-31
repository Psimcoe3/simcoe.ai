[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExportMullions Property

---



|  |
| --- |
| [EnergyAnalysisDetailModelOptions Class](18297392-d94a-cdab-feb3-81482771c44d.htm)   [See Also](#seeAlsoToggle) |

Indicates if to specify the setting for exporting mullions.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public bool ExportMullions { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property ExportMullions As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool ExportMullions { 	bool get (); 	void set (bool value); } ``` |

# Remarks

When this setting is on, mullions will be exported as shading surfaces. A "simplified" analytical shading surface is produced from a mullion based on its centerline, thickness and offset.

# See Also

[EnergyAnalysisDetailModelOptions Class](18297392-d94a-cdab-feb3-81482771c44d.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)