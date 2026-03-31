[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AnalyzeEnclosedSpaceVolumes Property

---



|  |
| --- |
| [BuildingEnvelopeAnalyzerOptions Class](2a20b547-06bb-360c-c977-24466b56386a.htm)   [See Also](#seeAlsoToggle) |

Whether or not to analyze interior connected regions inside the building forming enclosed space volumes.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public bool AnalyzeEnclosedSpaceVolumes { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property AnalyzeEnclosedSpaceVolumes As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool AnalyzeEnclosedSpaceVolumes { 	bool get (); 	void set (bool value); } ``` |

# Remarks

If true, the analyzer will also look for bounding building elements and connected analytical grid cells for enclosed space volumes inside the building.

# See Also

[BuildingEnvelopeAnalyzerOptions Class](2a20b547-06bb-360c-c977-24466b56386a.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)