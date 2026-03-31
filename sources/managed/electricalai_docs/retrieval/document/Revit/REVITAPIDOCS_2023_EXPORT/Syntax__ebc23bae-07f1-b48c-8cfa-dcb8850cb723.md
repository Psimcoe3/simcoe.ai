[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MergeRegionsAdjacentToSegment Method

---



|  |
| --- |
| [CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.htm)   [See Also](#seeAlsoToggle) |

Merges the two regions which share the specified segment.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public int MergeRegionsAdjacentToSegment( 	int segmentId, 	int layerIdxForMergedRegion ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function MergeRegionsAdjacentToSegment ( _ 	segmentId As Integer, _ 	layerIdxForMergedRegion As Integer _ ) As Integer ``` |

 

| Visual C++ |
| --- |
| ``` public: int MergeRegionsAdjacentToSegment( 	int segmentId,  	int layerIdxForMergedRegion ) ``` |

#### Parameters

segmentId
:   Type:  System Int32    
     The id of a segment in the underlying grid.

layerIdxForMergedRegion
:   Type:  System Int32    
     The index of the layer to which the resulting region will be associated.

#### Return Value

The id of the resulting region. If -1 is returned, then the operation would have produced an invalid region and was not performed.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The layer index is out of range. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Split and merge regions operations can be used only for vertically compound structures without variable thickness layers. -or- The segment is not shared by adjacent regions. |

# See Also

[CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)