[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ChangeRegionWidth Method

---



|  |
| --- |
| [CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.htm)   [See Also](#seeAlsoToggle) |

Adjust the width of an existing simple region.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool ChangeRegionWidth( 	int regionId, 	double newWidth ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function ChangeRegionWidth ( _ 	regionId As Integer, _ 	newWidth As Double _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool ChangeRegionWidth( 	int regionId,  	double newWidth ) ``` |

#### Parameters

regionId
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The id of a region.

newWidth
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The desired width of the specified region.

#### Return Value

True if newWidth is zero and the region was deleted.

# Remarks

If width is changed to zero, the effect is to delete the region.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | It is not a valid region id. -or- It is not a simple region. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This operation is valid only for vertically compound structures. |

# See Also

[CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)