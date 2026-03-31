[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CanLayerWidthBeNonZero Method

---



|  |
| --- |
| [CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.htm)   [See Also](#seeAlsoToggle) |

Identifies if changing the width of an existing layer from zero to a positive value will create a rectangular region.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool CanLayerWidthBeNonZero( 	int layerIdx ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function CanLayerWidthBeNonZero ( _ 	layerIdx As Integer _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool CanLayerWidthBeNonZero( 	int layerIdx ) ``` |

#### Parameters

layerIdx
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The index of a CompoundStructureLayer.

# Remarks

This is only allowed if there is a vertical line such that all regions to the left are assigned to layers with index < layerIdx, and all regions to the right are assigned to layers with index > layerIdx.

# See Also

[CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)