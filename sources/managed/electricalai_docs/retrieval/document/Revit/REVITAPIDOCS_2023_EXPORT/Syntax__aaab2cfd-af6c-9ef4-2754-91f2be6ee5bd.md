[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CanHaveOrdinateDimensionSetting Method

---



|  |
| --- |
| [DimensionType Class](a6f6655d-3383-a0ea-670d-0bbe6d2bb964.htm)   [See Also](#seeAlsoToggle) |

Checks whether this DimensionType can have an ordinate dimension settings.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)

# Syntax

| C# |
| --- |
| ``` public bool CanHaveOrdinateDimensionSetting() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function CanHaveOrdinateDimensionSetting As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool CanHaveOrdinateDimensionSetting() ``` |

#### Return Value

True when the DimensionType is linear and the Dimension String Type parameter is ordinate, false otherwise.

# Remarks

It returns true when the DimensionType is linear and when Dimension String Type parameter is set to Ordinate.

# See Also

[DimensionType Class](a6f6655d-3383-a0ea-670d-0bbe6d2bb964.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)