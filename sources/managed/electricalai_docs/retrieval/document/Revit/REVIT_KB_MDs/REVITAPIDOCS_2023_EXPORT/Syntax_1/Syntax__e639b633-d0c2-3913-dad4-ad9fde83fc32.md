[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetHookPlaneNormalForBarIdx Method

---



|  |
| --- |
| [RebarUpdateCurvesData Class](ff847aea-8397-8b79-b039-16a72e479c9f.htm)   [See Also](#seeAlsoToggle) |

Set the normal of plane in which the hook at end of bar with index barPositionIndex will stay. This information is set to the rebar after the API execution is finished successfully.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public void SetHookPlaneNormalForBarIdx( 	int end, 	int barPositionIndex, 	XYZ hookNormal ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetHookPlaneNormalForBarIdx ( _ 	end As Integer, _ 	barPositionIndex As Integer, _ 	hookNormal As XYZ _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetHookPlaneNormalForBarIdx( 	int end,  	int barPositionIndex,  	XYZ^ hookNormal ) ``` |

#### Parameters

end
:   Type:  System Int32    
     The end of bar. Should be 0 for start or 1 for end.

barPositionIndex
:   Type:  System Int32    
     Index of the bar for which it will set hook plane normal.

hookNormal
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The normal of plane in which the hook at end of bar with index barPositionIndex will stay.

# Remarks

This information is set to the rebar after the API execution is finished successfully. Before setting the value a validation will be done. We consider a hook plane normal valid if it isn't parallel with the bar direction at end.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | Invalid end. -or- hookNormal has zero length. |

# See Also

[RebarUpdateCurvesData Class](ff847aea-8397-8b79-b039-16a72e479c9f.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)