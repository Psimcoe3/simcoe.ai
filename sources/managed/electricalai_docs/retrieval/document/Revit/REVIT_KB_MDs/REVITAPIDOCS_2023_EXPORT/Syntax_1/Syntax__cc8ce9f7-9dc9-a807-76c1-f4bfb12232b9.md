[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidCurveLoop Method

---



|  |
| --- |
| [MultiSegmentGrid Class](8488ef7c-7669-26a7-8088-dd78e96850de.htm)   [See Also](#seeAlsoToggle) |

Identifies whether the specified curve loop is valid for creation of a MultiSegmentGrid.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static bool IsValidCurveLoop( 	CurveLoop curveLoop ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsValidCurveLoop ( _ 	curveLoop As CurveLoop _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsValidCurveLoop( 	CurveLoop^ curveLoop ) ``` |

#### Parameters

curveLoop
:   Type:  [Autodesk.Revit.DB CurveLoop](84824924-cb89-9e20-de6e-3461f429dfd6.htm)    
     The curve loop.

#### Return Value

True if the curve loop is an open curve loop consisting of lines and arcs, and false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[MultiSegmentGrid Class](8488ef7c-7669-26a7-8088-dd78e96850de.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)