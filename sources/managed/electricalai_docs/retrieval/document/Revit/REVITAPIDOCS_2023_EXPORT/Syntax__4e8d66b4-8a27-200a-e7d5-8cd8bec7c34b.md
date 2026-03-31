[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsBarMatchedWithShapeInReverseOrder Method

---



|  |
| --- |
| [RebarFreeFormAccessor Class](bf146aa3-f780-646e-c3cd-42e7a61d18e6.htm)   [See Also](#seeAlsoToggle) |

Checks if the bar at index barPositionIndex it's matched in reversed order with its shape.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 19.0.0.0 (19.0.0.405)   
  **Since:**  2019

# Syntax

| C# |
| --- |
| ``` public bool IsBarMatchedWithShapeInReverseOrder( 	int barPositionIndex ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsBarMatchedWithShapeInReverseOrder ( _ 	barPositionIndex As Integer _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsBarMatchedWithShapeInReverseOrder( 	int barPositionIndex ) ``` |

#### Parameters

barPositionIndex
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     An index between 0 and (NumberOfBarPositions-1).

#### Return Value

Returns true if the bar is matched in reversed order with its shape, false otherwise.

# Remarks

If this Rebar has Workshop Instructions set to Straight will return false for all barPositionIndex between 0 and (NumberOfBarPositions-1).

If this Rebar has Workshop Instructions set to Bent there are different cases:

* All bars are matched exactly with a shape. In this case will return false for all barPositionIndex between 0 and (NumberOfBarPositions-1).
* All bars are matched in reversed order with a shape. In this case the Rebar will be reversed and will return false for all barPositionIndex between 0 and (NumberOfBarPositions-1).
* Some bars are matched in reversed order and the others are matched exactly with a shape. For the bars matched in reversed order will return true and for the others will return false

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | barPositionIndex is not in the range [ 0, NumberOfBarPositions-1 ]. |

# See Also

[RebarFreeFormAccessor Class](bf146aa3-f780-646e-c3cd-42e7a61d18e6.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)