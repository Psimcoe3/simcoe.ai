[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetProjectionType Method

---



|  |
| --- |
| [CurveByPointsUtils Class](20dd9f72-4653-4ea8-6397-af04e5093fbe.htm)   [See Also](#seeAlsoToggle) |

Sets the projection type of the CurveElement.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static void SetProjectionType( 	CurveElement curveElem, 	CurveProjectionType value ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Sub SetProjectionType ( _ 	curveElem As CurveElement, _ 	value As CurveProjectionType _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: static void SetProjectionType( 	CurveElement^ curveElem,  	CurveProjectionType value ) ``` |

#### Parameters

curveElem
:   Type:  [Autodesk.Revit.DB CurveElement](61673852-2d08-003d-e9fd-4be89d533774.htm)    
     The CurveElement.

value
:   Type:  [Autodesk.Revit.DB CurveProjectionType](5669d7b4-2440-877f-5889-9390af7f8542.htm)    
     The input projection type.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The input CurveElement is not a CurveByPoints. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[CurveByPointsUtils Class](20dd9f72-4653-4ea8-6397-af04e5093fbe.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)