[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Origin Property

---



|  |
| --- |
| [ColorFillLegend Class](81cbdc7c-9f7f-b454-5669-77ca0514eda7.htm)   [See Also](#seeAlsoToggle) |

The top left corner of the color fill legend.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public XYZ Origin { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Origin As XYZ 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property XYZ^ Origin { 	XYZ^ get (); 	void set (XYZ^ value); } ``` |

# Remarks

The origin point must be on the view plane this legend is placed on.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The origin is not on the view plane that this legend is placed on. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[ColorFillLegend Class](81cbdc7c-9f7f-b454-5669-77ca0514eda7.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)