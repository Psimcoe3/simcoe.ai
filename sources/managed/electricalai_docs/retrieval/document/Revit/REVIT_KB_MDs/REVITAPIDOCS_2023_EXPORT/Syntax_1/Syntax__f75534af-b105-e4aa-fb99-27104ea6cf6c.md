[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetHookOrientationAngleAtIndex Method

---



|  |
| --- |
| [RebarFreeFormAccessor Class](bf146aa3-f780-646e-c3cd-42e7a61d18e6.htm)   [See Also](#seeAlsoToggle) |

Gets the hook orientation angle that is applied to this Rebar at the bar with index barPositionIndex at the specified end.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 19.0.0.0 (19.0.0.405)   
  **Since:**  2019

# Syntax

| C# |
| --- |
| ``` public double GetHookOrientationAngleAtIndex( 	int barPositionIndex, 	int end ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetHookOrientationAngleAtIndex ( _ 	barPositionIndex As Integer, _ 	end As Integer _ ) As Double ``` |

 

| Visual C++ |
| --- |
| ``` public: double GetHookOrientationAngleAtIndex( 	int barPositionIndex,  	int end ) ``` |

#### Parameters

barPositionIndex
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     An index between 0 and (NumberOfBarPositions-1).

end
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     0 for the start hook, 1 for the end hook.

#### Return Value

Returns the hook orientation angle at the specified end.

# Remarks

If this Rebar has Workshop Instructions set to Straight will return the same value for all barPositionIndex between 0 and (NumberOfBarPositions-1). This value will be the same as RebarFreeFormAccessor.GetHookOrientationAngle(int end).

If this Rebar has Workshop Instructions set to Bent there are different cases:

* All bars are matched exactly with a shape. In this case will return the same value for all barPositionIndex between 0 and (NumberOfBarPositions-1). This value will be the same as RebarFreeFormAccessor.GetHookOrientationAngle(int end).
* All bars are matched in reversed order with a shape. In this case will return the same value for all barPositionIndex between 0 and (NumberOfBarPositions-1). This value will be the same as RebarFreeFormAccessor.GetHookOrientationAngle(int end).
* Some bars are matched in reversed order and the others are matched exactly with a shape. In this case for bars that are matched reversed will return the hook orientation angle at the opposite end. For the others bars will return the same as RebarFreeFormAccessor.GetHookOrientationAngle(int end).

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | end must be 0 or 1. -or- barPositionIndex is not in the range [ 0, NumberOfBarPositions-1 ]. |

# See Also

[RebarFreeFormAccessor Class](bf146aa3-f780-646e-c3cd-42e7a61d18e6.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)