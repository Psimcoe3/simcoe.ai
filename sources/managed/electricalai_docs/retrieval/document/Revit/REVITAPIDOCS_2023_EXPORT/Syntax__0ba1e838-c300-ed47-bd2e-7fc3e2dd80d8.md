[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SplitVolumes Method

---



|  |
| --- |
| [SolidUtils Class](4c285bc6-c14e-9d55-5295-138764c01d12.htm)   [See Also](#seeAlsoToggle) |

Splits a solid geometry into several separate solids.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static IList<Solid> SplitVolumes( 	Solid solid ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function SplitVolumes ( _ 	solid As Solid _ ) As IList(Of Solid) ``` |

 

| Visual C++ |
| --- |
| ``` public: static IList<Solid^>^ SplitVolumes( 	Solid^ solid ) ``` |

#### Parameters

solid
:   Type:  [Autodesk.Revit.DB Solid](7a3b5ac1-c66d-9f81-a11d-9bcd4e026295.htm)    
     The solid.

#### Return Value

The split solid geometries.

# Remarks

If no splitting is done, a copy of the input solid will be returned in the output array.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Failed to split the solid geometry. |

# See Also

[SolidUtils Class](4c285bc6-c14e-9d55-5295-138764c01d12.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)