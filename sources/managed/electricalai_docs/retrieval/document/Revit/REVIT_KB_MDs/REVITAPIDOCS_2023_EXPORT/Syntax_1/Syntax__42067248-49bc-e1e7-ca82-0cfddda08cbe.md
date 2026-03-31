[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GridCellSize Property

---



|  |
| --- |
| [BuildingEnvelopeAnalyzerOptions Class](2a20b547-06bb-360c-c977-24466b56386a.htm)   [See Also](#seeAlsoToggle) |

The cell size for the uniform cubical grid used when analyzing the building envelope.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public double GridCellSize { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property GridCellSize As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double GridCellSize { 	double get (); 	void set (double value); } ``` |

# Remarks

This is the base size of the "cubes" used to divide the building shell bounding box into a uniform cubical 3D grid. If this overrideGridCellSize option is set, this exact value will be used for the grid cell size. The cell size should be specified in the length unit for the Revit project.

# See Also

[BuildingEnvelopeAnalyzerOptions Class](2a20b547-06bb-360c-c977-24466b56386a.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)