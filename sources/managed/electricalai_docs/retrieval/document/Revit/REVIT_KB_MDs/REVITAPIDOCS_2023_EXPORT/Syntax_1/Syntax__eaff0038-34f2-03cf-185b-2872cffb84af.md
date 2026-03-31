[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetCurveInView Method

---



|  |
| --- |
| [DatumPlane Class](3e0a6725-ee40-c4d5-839f-b7720c1fe2af.htm)   [See Also](#seeAlsoToggle) |

Sets the extents to match the curve.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public void SetCurveInView( 	DatumExtentType extentMode, 	View view, 	Curve curve ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetCurveInView ( _ 	extentMode As DatumExtentType, _ 	view As View, _ 	curve As Curve _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetCurveInView( 	DatumExtentType extentMode,  	View^ view,  	Curve^ curve ) ``` |

#### Parameters

extentMode
:   Type:  [Autodesk.Revit.DB DatumExtentType](7a968bc3-1860-6a8b-6f3a-2b23b80a56a5.htm)    
     The extent type.

view
:   Type:  [Autodesk.Revit.DB View](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)    
     The view.

curve
:   Type:  [Autodesk.Revit.DB Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)    
     The curve.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The datum plane cannot be visible in the view. -or- The curve is unbound or not coincident with the original one of the datum plane. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[DatumPlane Class](3e0a6725-ee40-c4d5-839f-b7720c1fe2af.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)