[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetProjectionType Method

---



|  |
| --- |
| [CurveByPointsUtils Class](20dd9f72-4653-4ea8-6397-af04e5093fbe.htm)   [See Also](#seeAlsoToggle) |

Gets the projection type of the CurveElement.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static CurveProjectionType GetProjectionType( 	CurveElement curveElem ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetProjectionType ( _ 	curveElem As CurveElement _ ) As CurveProjectionType ``` |

 

| Visual C++ |
| --- |
| ``` public: static CurveProjectionType GetProjectionType( 	CurveElement^ curveElem ) ``` |

#### Parameters

curveElem
:   Type:  [Autodesk.Revit.DB CurveElement](61673852-2d08-003d-e9fd-4be89d533774.htm)    
     The CurveElement.

#### Return Value

The projection type.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The input CurveElement is not a CurveByPoints. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[CurveByPointsUtils Class](20dd9f72-4653-4ea8-6397-af04e5093fbe.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)