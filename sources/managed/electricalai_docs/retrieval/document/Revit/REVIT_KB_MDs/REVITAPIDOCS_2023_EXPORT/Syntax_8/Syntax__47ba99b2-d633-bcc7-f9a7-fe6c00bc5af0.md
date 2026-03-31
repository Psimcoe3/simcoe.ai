[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetLayerWidth Method

---



|  |
| --- |
| [CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.htm)   [See Also](#seeAlsoToggle) |

Retrieves the width of a specified layer.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public double GetLayerWidth( 	int layerIdx ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetLayerWidth ( _ 	layerIdx As Integer _ ) As Double ``` |

 

| Visual C++ |
| --- |
| ``` public: double GetLayerWidth( 	int layerIdx ) ``` |

#### Parameters

layerIdx
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     Index of a layer in the CompoundStructure.

#### Return Value

The width of the specified layer.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The layer index is out of range. |

# See Also

[CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)