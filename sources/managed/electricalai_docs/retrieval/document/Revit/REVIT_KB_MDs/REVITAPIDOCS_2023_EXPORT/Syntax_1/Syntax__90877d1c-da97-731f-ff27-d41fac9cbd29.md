[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DimensionLineLength Property

---



|  |
| --- |
| [OrdinateDimensionSetting Class](d146dae8-f2d4-9102-201a-4756759410d0.htm)   [See Also](#seeAlsoToggle) |

Specifies the dimension line segment length. This setting is enabled when Dimension Line Style is Segmented.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2017 Subscription Update

# Syntax

| C# |
| --- |
| ``` public double DimensionLineLength { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property DimensionLineLength As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double DimensionLineLength { 	double get (); 	void set (double value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The given value for dimensionLineLength must be greater than 0 and no more than 30000 feet. |

# See Also

[OrdinateDimensionSetting Class](d146dae8-f2d4-9102-201a-4756759410d0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)