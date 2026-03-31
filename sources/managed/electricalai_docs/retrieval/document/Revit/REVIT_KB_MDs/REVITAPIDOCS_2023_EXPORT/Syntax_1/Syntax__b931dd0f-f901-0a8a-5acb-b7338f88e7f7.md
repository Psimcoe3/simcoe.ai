[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### OriginatingElementDescription Property

---



|  |
| --- |
| [EnergyAnalysisOpening Class](825025c8-342d-46b7-592e-e42d8f8e8336.htm)   [See Also](#seeAlsoToggle) |

The description for the originating Revit element.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public string OriginatingElementDescription { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property OriginatingElementDescription As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ OriginatingElementDescription { 	String^ get (); } ``` |

# Remarks

Surface and Opening elements get an CADObjectId element assigned according to the below described schema, based on associative room bounding element:

(Family Name): (Family Type)[Element Id]

Sample: System Panel: System Panel [50566]

# See Also

[EnergyAnalysisOpening Class](825025c8-342d-46b7-592e-e42d8f8e8336.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)