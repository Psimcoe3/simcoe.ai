[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DefaultFamilyType Property

---



|  |
| --- |
| [ComponentRepeater Class](27dbc5bd-40e7-c044-11e6-7053adf92c6f.htm)   [See Also](#seeAlsoToggle) |

The default family type for the component repeater.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public ElementId DefaultFamilyType { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property DefaultFamilyType As ElementId 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ DefaultFamilyType { 	ElementId^ get (); 	void set (ElementId^ value); } ``` |

# Remarks

The default family type is the type of the instances in default slots. This includes slots that are added when the repeater grows. When setting this property, all slots with instances of the default type will change their components to an instance of the new default type. Empty slots will remain unchanged. Slots with non-default family instances will remain unchanged.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: Invalid type for the repeater. The type must be an adaptive family with no shape handles. In addition, it must have same category and same number of placement points as the current type of the repeater. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[ComponentRepeater Class](27dbc5bd-40e7-c044-11e6-7053adf92c6f.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)