[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetSplitRegionOffset Method

---



|  |
| --- |
| [ViewCropRegionShapeManager Class](2610cb66-5dae-9fc8-4e83-7dfe88085abb.htm)   [See Also](#seeAlsoToggle) |

Returns the offset for the specified split crop region.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public XYZ GetSplitRegionOffset( 	int regionIndex ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetSplitRegionOffset ( _ 	regionIndex As Integer _ ) As XYZ ``` |

 

| Visual C++ |
| --- |
| ``` public: XYZ^ GetSplitRegionOffset( 	int regionIndex ) ``` |

#### Parameters

regionIndex
:   Type:  System Int32    
     Index of the split crop region (numbering starts with 0).

#### Return Value

A vector in model space representing the offset which is applied to the split crop region's boundary.

# Remarks

The points in the split crop region's boundary are not in model space. Add the offset returned by this method to each point in the crop region's boundary to transform the points into model space coordinates.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The provided region index is invalid. |

# See Also

[ViewCropRegionShapeManager Class](2610cb66-5dae-9fc8-4e83-7dfe88085abb.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)