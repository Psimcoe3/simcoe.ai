[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NewCurveLoopsProfile Method

---



|  |
| --- |
| [Application Class](5e11e5bf-82da-ae9b-1c52-95d0e9f28c96.htm)   [See Also](#seeAlsoToggle) |

Creates a new CurveLoopsProfile object.

**Namespace:**   [Autodesk.Revit.Creation](ded320da-058a-4edd-0418-0582389559a7.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public CurveLoopsProfile NewCurveLoopsProfile( 	CurveArrArray curveLoops ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function NewCurveLoopsProfile ( _ 	curveLoops As CurveArrArray _ ) As CurveLoopsProfile ``` |

 

| Visual C++ |
| --- |
| ``` public: CurveLoopsProfile^ NewCurveLoopsProfile( 	CurveArrArray^ curveLoops ) ``` |

#### Parameters

curveLoops
:   Type:  [Autodesk.Revit.DB CurveArrArray](c9d071fe-9724-42ed-e280-57381cd44301.htm)    
     The curve loops of the Profile.

#### Return Value

The new CurveLoopsProfile object.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the argument is    a null reference (  Nothing  in Visual Basic)  . |

# See Also

[Application Class](5e11e5bf-82da-ae9b-1c52-95d0e9f28c96.htm)

[Autodesk.Revit.Creation Namespace](ded320da-058a-4edd-0418-0582389559a7.htm)