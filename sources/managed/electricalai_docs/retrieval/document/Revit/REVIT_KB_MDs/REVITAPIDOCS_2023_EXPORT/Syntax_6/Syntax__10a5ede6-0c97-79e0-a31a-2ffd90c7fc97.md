[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetBoxCenter Method

---



|  |
| --- |
| [Viewport Class](5991dc40-234a-4835-cc06-07524d2e61a4.htm)   [See Also](#seeAlsoToggle) |

Returns the center of the outline of the viewport on the sheet, excluding the viewport label.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public XYZ GetBoxCenter() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetBoxCenter As XYZ ``` |

 

| Visual C++ |
| --- |
| ``` public: XYZ^ GetBoxCenter() ``` |

#### Return Value

The center of the outline of the viewport on the sheet.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The viewport is not on a sheet. |

# See Also

[Viewport Class](5991dc40-234a-4835-cc06-07524d2e61a4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)