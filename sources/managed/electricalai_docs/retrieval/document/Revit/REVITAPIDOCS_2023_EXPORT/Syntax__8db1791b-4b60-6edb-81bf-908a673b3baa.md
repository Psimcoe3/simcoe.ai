[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SplitRegion Method (UV, RectangularGridSegmentOrientation)

---



|  |
| --- |
| [CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.htm)   [See Also](#seeAlsoToggle) |

Splits the region which contains the specified grid point by a line with the specified direction.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public int SplitRegion( 	UV gridUV, 	RectangularGridSegmentOrientation splitDirection ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function SplitRegion ( _ 	gridUV As UV, _ 	splitDirection As RectangularGridSegmentOrientation _ ) As Integer ``` |

 

| Visual C++ |
| --- |
| ``` public: int SplitRegion( 	UV^ gridUV,  	RectangularGridSegmentOrientation splitDirection ) ``` |

#### Parameters

gridUV
:   Type:  [Autodesk.Revit.DB UV](1724be37-059b-91ff-aa74-d1508082f76d.htm)    
     Coordinates of a point in the rectangular grid of this compound structure.

splitDirection
:   Type:  [Autodesk.Revit.DB RectangularGridSegmentOrientation](cc712c10-e391-eaf3-0441-ecc183f26846.htm)    
     Specifies the direction of the split.

#### Return Value

The id of the region created by this operation.

# Remarks

This method is meant to be used in conjunction with  [FindEnclosingRegionAndSegments(UV, RectangularGridSegmentOrientation, Int32 , Int32 )](e5a63d60-6fa3-f414-20b5-ef72da637849.htm)  . Grid coordinates correspond to uv coordinates of faces.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Split and merge regions operations can be used only for vertically compound structures without variable thickness layers. |

# See Also

[CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.htm)

[SplitRegion Overload](43f7d4f1-ec9d-7e15-c9d2-8f7cc2659fef.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)