[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetBarPositionTransform Method

---



|  |
| --- |
| [RebarShapeDrivenAccessor Class](6d2f77e7-bbe2-5bd5-723a-bf27c3df1a65.htm)   [See Also](#seeAlsoToggle) |

Return a transform representing the relative position of any individual bar in the set.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public Transform GetBarPositionTransform( 	int barPositionIndex ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetBarPositionTransform ( _ 	barPositionIndex As Integer _ ) As Transform ``` |

 

| Visual C++ |
| --- |
| ``` public: Transform^ GetBarPositionTransform( 	int barPositionIndex ) ``` |

#### Parameters

barPositionIndex
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     An index between 0 and (NumberOfBarPositions-1).

#### Return Value

The position of a bar in the set relative to the first position.

# Remarks

The transform is a translation along the distribution path. It can be applied to the results of GetCenterlineCurves() to produce any bar in the rebar set. For barPositionIndex=0, the identity transform is always returned.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | barPositionIndex is not in the range [ 0, NumberOfBarPositions-1 ]. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This RebarShapeDrivenAccessor doesn't contain a valid rebar reference. |

# See Also

[RebarShapeDrivenAccessor Class](6d2f77e7-bbe2-5bd5-723a-bf27c3df1a65.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)