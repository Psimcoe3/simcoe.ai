[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Area Property

---



|  |
| --- |
| [EnergyAnalysisSpace Class](cd0567d0-f5e0-a850-6d10-bde911831947.htm)   [See Also](#seeAlsoToggle) |

The area for this space.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public double Area { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Area As Double 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property double Area { 	double get (); } ``` |

# Remarks

If the space is created with the mode 'Use Rooms or Spaces', this value is the enclosed area measured by interior bounding surfaces. Otherwise, this value is measured by the center plane of walls and the top plane of roofs and floors.

# See Also

[EnergyAnalysisSpace Class](cd0567d0-f5e0-a850-6d10-bde911831947.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)