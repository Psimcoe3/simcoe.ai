[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetColumnWidths Method

---



|  |
| --- |
| [ColorFillLegend Class](81cbdc7c-9f7f-b454-5669-77ca0514eda7.htm)   [See Also](#seeAlsoToggle) |

Sets array of column widths.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public void SetColumnWidths( 	IList<double> widths ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetColumnWidths ( _ 	widths As IList(Of Double) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetColumnWidths( 	IList<double>^ widths ) ``` |

#### Parameters

widths
:   Type:  System.Collections.Generic IList   Double

# Remarks

Input array length must be the same as what  [GetColumnWidths](bea0b37a-991b-8ddc-28d7-0bacf0f4181a.htm)  returns. It can only contain positive values.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Array is not valid. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ColorFillLegend Class](81cbdc7c-9f7f-b454-5669-77ca0514eda7.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)