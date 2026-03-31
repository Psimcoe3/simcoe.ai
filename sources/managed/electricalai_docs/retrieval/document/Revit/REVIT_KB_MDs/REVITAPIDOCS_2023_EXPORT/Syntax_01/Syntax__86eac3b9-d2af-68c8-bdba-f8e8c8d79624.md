[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddBarGeometry Method (CurveLoop)

---



|  |
| --- |
| [RebarCurvesData Class](71996f44-c8f9-7695-ccb9-efae09726c9c.htm)   [See Also](#seeAlsoToggle) |

Adds a new bar to the new rebar geometry. This information is set to the rebar after the API execution is finished successfully.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public RebarFreeFormValidationResult AddBarGeometry( 	CurveLoop curves ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function AddBarGeometry ( _ 	curves As CurveLoop _ ) As RebarFreeFormValidationResult ``` |

 

| Visual C++ |
| --- |
| ``` public: RebarFreeFormValidationResult AddBarGeometry( 	CurveLoop^ curves ) ``` |

#### Parameters

curves
:   Type:  [Autodesk.Revit.DB CurveLoop](84824924-cb89-9e20-de6e-3461f429dfd6.htm)    
     Curves describing one bar in the set.

#### Return Value

Returns Success if everything is ok, otherwise the failure reason.

# Remarks

This function can fail due to following reasons:

* CurveLoop is empty.
* CurveLoop contains an unbounded curve.
* A rebar constructed from curves can't be bent according to the bending radius.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Incorrect number of bar geometry for the current layout. |

# See Also

[RebarCurvesData Class](71996f44-c8f9-7695-ccb9-efae09726c9c.htm)

[AddBarGeometry Overload](8c068768-a57c-28fe-80a4-7f22346e46a8.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)