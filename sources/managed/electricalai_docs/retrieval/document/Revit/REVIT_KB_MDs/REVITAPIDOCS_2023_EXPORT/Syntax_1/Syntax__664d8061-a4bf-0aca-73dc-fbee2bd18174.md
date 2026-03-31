[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CropBoxVisible Property

---



|  |
| --- |
| [View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)   [See Also](#seeAlsoToggle) |

Whether or not the Crop Box/Region is visible for the view.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool CropBoxVisible { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property CropBoxVisible As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool CropBoxVisible { 	bool get (); 	void set (bool value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InapplicableDataException](dc1a6d15-8923-a1fe-722a-4e976634a519.htm) | Thrown when getting this property, if the view is a template and cannot have a crop box applied. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when setting this property, if the view is a template and cannot have a crop box applied. |

# See Also

[View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)