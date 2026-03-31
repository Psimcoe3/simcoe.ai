[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Export2DGeometricObjectsIncludingPatternLines Property

---



|  |
| --- |
| [CustomExporter Class](d2437433-9183-cbb1-1c67-dedd86db5b5a.htm)   [See Also](#seeAlsoToggle) |

This flag sets the exporter of 2D views to either include or exclude output of face pattern lines as part of geometric objects when the model is being processed by the export context.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2020

# Syntax

| C# |
| --- |
| ``` public bool Export2DGeometricObjectsIncludingPatternLines { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Export2DGeometricObjectsIncludingPatternLines As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool Export2DGeometricObjectsIncludingPatternLines { 	bool get (); 	void set (bool value); } ``` |

# Remarks

This flag is ignored if view has Wireframe display style. This flag is ignored unless property "IncludeGeometricObjects" is set to true.

# See Also

[CustomExporter Class](d2437433-9183-cbb1-1c67-dedd86db5b5a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)