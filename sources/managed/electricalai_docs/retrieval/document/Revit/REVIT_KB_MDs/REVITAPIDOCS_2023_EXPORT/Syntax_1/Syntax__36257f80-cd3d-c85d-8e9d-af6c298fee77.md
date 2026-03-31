[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Volume Property

---



|  |
| --- |
| [EnergyAnalysisSpace Class](cd0567d0-f5e0-a850-6d10-bde911831947.htm)   [See Also](#seeAlsoToggle) |

The volume for this space.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public double Volume { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Volume As Double 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property double Volume { 	double get (); } ``` |

# Remarks

If the space is created with the mode 'Use Rooms or Spaces', this value is the enclosed volume measured by interior bounding surfaces. Otherwise, this value is the average of the analytical volume and the voxel volume. Note that the analytical volume is measured by the center plane of walls and the top plane of roofs and floors, and the voxel volume is measured by the number of enclosed unit cubes.

# See Also

[EnergyAnalysisSpace Class](cd0567d0-f5e0-a850-6d10-bde911831947.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)