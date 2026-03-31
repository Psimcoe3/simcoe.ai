[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PathStart Property

---



|  |
| --- |
| [PathOfTravel Class](99c2bb04-151f-c325-84b2-40dee81447d6.htm)   [See Also](#seeAlsoToggle) |

The start point of the path. The Z coordinate will equal the view's level elevation. To update path calculations, call update.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2020

# Syntax

| C# |
| --- |
| ``` public XYZ PathStart { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property PathStart As XYZ 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property XYZ^ PathStart { 	XYZ^ get (); 	void set (XYZ^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | When setting this property: This functionality is not available in Revit LT. -or- When setting this property: Cannot perform this operation for a path of travel in a group. |

# See Also

[PathOfTravel Class](99c2bb04-151f-c325-84b2-40dee81447d6.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)