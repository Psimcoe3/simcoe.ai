[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LineShapeAtCorner Property

---



|  |
| --- |
| [StairsPathType Class](36994970-3d80-62a3-df6f-381d38f2eda0.htm)   [See Also](#seeAlsoToggle) |

The line shape of stairs path at the corner.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public StairsPathLineShapeAtCorner LineShapeAtCorner { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property LineShapeAtCorner As StairsPathLineShapeAtCorner 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property StairsPathLineShapeAtCorner LineShapeAtCorner { 	StairsPathLineShapeAtCorner get (); 	void set (StairsPathLineShapeAtCorner value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | When setting this property: Either the stairs path direction is not AutomaticUpDown, or it is AlwaysUp but DrawForEachRun is false. |

# See Also

[StairsPathType Class](36994970-3d80-62a3-df6f-381d38f2eda0.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)