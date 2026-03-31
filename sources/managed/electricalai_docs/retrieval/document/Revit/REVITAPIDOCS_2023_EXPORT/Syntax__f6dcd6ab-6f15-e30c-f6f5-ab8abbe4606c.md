[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DrawForEachRun Property

---



|  |
| --- |
| [StairsPathType Class](36994970-3d80-62a3-df6f-381d38f2eda0.htm)   [See Also](#seeAlsoToggle) |

True if stairs paths should be drawn for each run, false if it should be drawn for the whole stairs.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public bool DrawForEachRun { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property DrawForEachRun As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool DrawForEachRun { 	bool get (); 	void set (bool value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | When setting this property: The StairsPathType is not fixed up direction so the data being set is not applicable. |

# See Also

[StairsPathType Class](36994970-3d80-62a3-df6f-381d38f2eda0.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)