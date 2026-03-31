[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RevisionCloudSpacing Property

---



|  |
| --- |
| [RevisionSettings Class](599f75fc-d2b6-63b3-7295-0c314415b638.htm)   [See Also](#seeAlsoToggle) |

Determines the size in paper space of revision clouds drawn in a project.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public double RevisionCloudSpacing { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property RevisionCloudSpacing As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double RevisionCloudSpacing { 	double get (); 	void set (double value); } ``` |

# Remarks

Revision clouds in Revit are created based on a collection of sketched lines. Revit then generates a series of "cloud bumps" along those lines to create a cloud shape. This setting determines the minimum length between the start and end each "cloud bump" (measured along the line). For example, if this setting were 2" and the sketched line were 3" long, Revit would create only one 3" bump. If the line length was increased to 4", Revit would add two 2" ones. Note that a single "cloud bump" consists of two arcs of slightly different size. Revit will always draw at least one "cloud bump" for each sketched line.

This value will be interpreted by Revit in paper space rather than in model space so that all of the clouds are shown in a uniform way on a sheet.

This value will be rounded to a length that can be displayed according to the current project settings. The value may not be zero after rounding. This value may not exceed the maximum distance that can be represented as a length in Revit.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: desiredCloudSpacing is not a valid value for the cloud spacing. |

# See Also

[RevisionSettings Class](599f75fc-d2b6-63b3-7295-0c314415b638.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)