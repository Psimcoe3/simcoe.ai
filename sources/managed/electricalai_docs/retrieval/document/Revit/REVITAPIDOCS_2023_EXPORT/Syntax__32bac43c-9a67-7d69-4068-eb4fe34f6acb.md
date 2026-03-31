[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LeaderEnd Property

---



|  |
| --- |
| [SpatialElementTag Class](0a20cdd6-6e44-bc77-a4c3-2d35470ba911.htm)   [See Also](#seeAlsoToggle) |

The position of the leader's end.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public XYZ LeaderEnd { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property LeaderEnd As XYZ 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property XYZ^ LeaderEnd { 	XYZ^ get (); 	void set (XYZ^ value); } ``` |

# Remarks

Returns the end point of the tag leader. Leader end point must be located inside of a room, space or an area. Use Room.IsPointInRoom or Space.IsPointInSpace method to check whether the leaderEnd is located in the host element or not.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The point is located outside of the spatial element. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | There is no leader for this tag. -or- When setting this property: SpatialElementTag is pinned. -or- When setting this property: SpatialElementTag is orphaned. |

# See Also

[SpatialElementTag Class](0a20cdd6-6e44-bc77-a4c3-2d35470ba911.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)