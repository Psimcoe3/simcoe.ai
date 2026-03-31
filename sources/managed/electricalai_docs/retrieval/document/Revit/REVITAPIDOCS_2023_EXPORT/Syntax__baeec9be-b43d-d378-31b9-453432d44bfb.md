[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BreakCurve Method

---



|  |
| --- |
| [MechanicalUtils Class](f7cbd23a-1b69-d9bf-88b4-df10a8c4be0b.htm)   [See Also](#seeAlsoToggle) |

Breaks the duct curve into two parts at the given position.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public static ElementId BreakCurve( 	Document document, 	ElementId ductId, 	XYZ ptBreak ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function BreakCurve ( _ 	document As Document, _ 	ductId As ElementId, _ 	ptBreak As XYZ _ ) As ElementId ``` |

 

| Visual C++ |
| --- |
| ``` public: static ElementId^ BreakCurve( 	Document^ document,  	ElementId^ ductId,  	XYZ^ ptBreak ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

ductId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The element id of the duct curve to break.

ptBreak
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The break point on the duct curve.

#### Return Value

The new duct curve element id if successful otherwise if a failure occurred an invalidElementId is returned.

# Remarks

This method is not applicable for breaking the flex duct.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | "The element is neither a duct nor a duct placeholder." -or- "The given point is not on the duct curve." |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[MechanicalUtils Class](f7cbd23a-1b69-d9bf-88b4-df10a8c4be0b.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)