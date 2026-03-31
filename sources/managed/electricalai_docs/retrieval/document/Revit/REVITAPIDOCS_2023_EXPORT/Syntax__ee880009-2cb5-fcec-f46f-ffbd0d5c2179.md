[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GridAspectRatio Property

---



|  |
| --- |
| [OBJExportOptions Class](fe6a5fe3-737a-1d30-fa65-37cc84e6e9d5.htm)   [See Also](#seeAlsoToggle) |

The maximum aspect ratio allowed in the grid placed across the face. The minimum allowed value is 1.0. The maximum allowed value is 10.0. By default this property is ignored.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public double GridAspectRatio { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property GridAspectRatio As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double GridAspectRatio { 	double get (); 	void set (double value); } ``` |

# Remarks

This property can be set by using export resolution type (by creation of OBJExportOptions or using  [!:Autodesk::Revit::DB::OBJExportOptions::setTessellationSettings(ExportResolution::Enum)]  method). In the case of Fine, Medium and Coarse resolutions, this property has the same value (10.0) and it is considered as explicitly set by the user. In the case of Custom resolution type, this property is only allowed to be obtained if it has been explicitly set.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The value gridAspectRatio is outside the allowable range of values for GridAspectRatio tessellation parameter. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | GridAspectRatio tessellation parameter is default (hasn't been explicitly set by the user) and cannot be obtained now. |

# See Also

[OBJExportOptions Class](fe6a5fe3-737a-1d30-fa65-37cc84e6e9d5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)