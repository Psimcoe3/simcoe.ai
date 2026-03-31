[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### OrientTo Method

---



|  |
| --- |
| [View3D Class](d795a238-fc24-1875-e64f-a2bef56ae949.htm)   [See Also](#seeAlsoToggle) |

Reorients the view to align with the forward direction.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public void OrientTo( 	XYZ forwardDirection ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub OrientTo ( _ 	forwardDirection As XYZ _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void OrientTo( 	XYZ^ forwardDirection ) ``` |

#### Parameters

forwardDirection
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The forward direction.

# Remarks

This method adjusts the ViewOrientation to align with the input forward direction. The eye position will be automatically determined based on the shape of the viewing area and size of the model. The UpDirection will be aligned with the project Z axis.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | forwardDirection has zero length. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | View is locked and cannot be reoriented. |

# See Also

[View3D Class](d795a238-fc24-1875-e64f-a2bef56ae949.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)