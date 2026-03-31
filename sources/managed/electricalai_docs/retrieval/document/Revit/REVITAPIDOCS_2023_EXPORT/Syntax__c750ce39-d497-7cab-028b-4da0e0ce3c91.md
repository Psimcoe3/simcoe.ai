[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RemoveSplitRegion Method

---



|  |
| --- |
| [ViewCropRegionShapeManager Class](2610cb66-5dae-9fc8-4e83-7dfe88085abb.htm)   [See Also](#seeAlsoToggle) |

Removes one region in split crop.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public void RemoveSplitRegion( 	int regionIndex ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub RemoveSplitRegion ( _ 	regionIndex As Integer _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void RemoveSplitRegion( 	int regionIndex ) ``` |

#### Parameters

regionIndex
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     Index of region to be deleted (numbering starts with 0).

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The provided region index cannot be deleted. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The crop of the associated view is not permitted to have multiple regions. -or- The view has non-rectangular crop shape set. |

# See Also

[ViewCropRegionShapeManager Class](2610cb66-5dae-9fc8-4e83-7dfe88085abb.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)