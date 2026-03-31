[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetSegmentOrientation Method

---



|  |
| --- |
| [CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.htm)   [See Also](#seeAlsoToggle) |

Gets the orientation of a segment.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public RectangularGridSegmentOrientation GetSegmentOrientation( 	int segmentId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetSegmentOrientation ( _ 	segmentId As Integer _ ) As RectangularGridSegmentOrientation ``` |

 

| Visual C++ |
| --- |
| ``` public: RectangularGridSegmentOrientation GetSegmentOrientation( 	int segmentId ) ``` |

#### Parameters

segmentId
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The id of a segment in this CompoundStructure.

#### Return Value

The orientation of the specified segment.

# Remarks

The boundaries of the regions of a vertically compound structure consist of vertical horizontal segments.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The segment id is invalid. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This operation is valid only for vertically compound structures. |

# See Also

[CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)