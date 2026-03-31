[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetLayerWidth Method

---



|  |
| --- |
| [CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.htm)   [See Also](#seeAlsoToggle) |

Sets the width of a specified layer.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public void SetLayerWidth( 	int layerIdx, 	double width ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetLayerWidth ( _ 	layerIdx As Integer, _ 	width As Double _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetLayerWidth( 	int layerIdx,  	double width ) ``` |

#### Parameters

layerIdx
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     Index of a layer in the CompoundStructure.

width
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The new width of the specified layer.

# Remarks

If the structure is vertically compound, and the layer is associated to a single simple region, the width of that region is adjusted. If layerIdx is 0 or LayerCount-1, and there is no associated region in the VerticalRegionsStructure, one will be created and associated to the layer. If the specified layer index is associated to a simple region, and the width is set to 0.0, that region will be deleted.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The width of the layer is not valid. |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The layer index is out of range. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | If the region of the layer is not a simple region. |

# See Also

[CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)