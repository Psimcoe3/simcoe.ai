[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Type Property

---



|  |
| --- |
| [EnergyAnalysisOpening Class](825025c8-342d-46b7-592e-e42d8f8e8336.htm)   [See Also](#seeAlsoToggle) |

The gbXML opening type attribute.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public gbXMLOpeningType Type { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Type As gbXMLOpeningType 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property gbXMLOpeningType Type { 	gbXMLOpeningType get (); } ``` |

# Remarks

The type of the opening is based on the family category for the opening and in what element it is contained in:

* If it is a Window it will have a type of OperableWindow.
* If it is a Door it will have a type of NonSlidingDoor.
* If the opening is contained in a Roof it will have a type of FixedSkylight.
* If it is a Curtain Wall Panel, the opening will default to a type of FixedWindow. If the material specified for the family, and the material transparency is less than 3%, the opening will be ignored as a solid panel.

An opening of the category Openings will have the type of Air.

# See Also

[EnergyAnalysisOpening Class](825025c8-342d-46b7-592e-e42d8f8e8336.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)