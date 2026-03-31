[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StraightLineMultiplier Property

---



|  |
| --- |
| [RebarHookType Class](3c7a78d5-f92b-e58b-e7c9-7927537498fd.htm)   [See Also](#seeAlsoToggle) |

Multiplier of bar diameter. Used to compute a default hook length. The default hook length can be overridden by the RebarBarType class.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public double StraightLineMultiplier { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property StraightLineMultiplier As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double StraightLineMultiplier { 	double get (); 	void set (double value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The given value for straightLineMultiplier is not a number |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: straightLineMultiplier must be greater than 0 and no more than 99. |

# See Also

[RebarHookType Class](3c7a78d5-f92b-e58b-e7c9-7927537498fd.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)