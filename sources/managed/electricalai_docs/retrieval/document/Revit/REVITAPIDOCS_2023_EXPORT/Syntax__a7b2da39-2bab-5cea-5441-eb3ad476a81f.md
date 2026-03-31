[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HasTangentJoin Method

---



|  |
| --- |
| [CurveElement Class](61673852-2d08-003d-e9fd-4be89d533774.htm)   [See Also](#seeAlsoToggle) |

Tests whether this curve element and the input curve element have common tangent join at the given end-point.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public bool HasTangentJoin( 	int end, 	ElementId other ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function HasTangentJoin ( _ 	end As Integer, _ 	other As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool HasTangentJoin( 	int end,  	ElementId^ other ) ``` |

#### Parameters

end
:   Type:  System Int32    
     Index of one of the curve's end. Values '0' and '1' indicate the start or end point, respectively.

other
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     ElementId of another Curve Element from the same document.

#### Return Value

Returns True if the two curve elements have a tangent join at the given end-point.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[CurveElement Class](61673852-2d08-003d-e9fd-4be89d533774.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)