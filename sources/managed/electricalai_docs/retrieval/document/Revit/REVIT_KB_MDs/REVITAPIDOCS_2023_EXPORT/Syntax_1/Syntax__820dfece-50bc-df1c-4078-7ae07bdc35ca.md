[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsLayerValid Method

---



|  |
| --- |
| [CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.htm)   [See Also](#seeAlsoToggle) |

Verifies that the data in this layer is internally consistent.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public bool IsLayerValid( 	int layerIdx, 	CompoundStructureLayer layer ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsLayerValid ( _ 	layerIdx As Integer, _ 	layer As CompoundStructureLayer _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsLayerValid( 	int layerIdx,  	CompoundStructureLayer^ layer ) ``` |

#### Parameters

layerIdx
:   Type:  System Int32    
     The index of the layer in the compound structure to be set.

layer
:   Type:  [Autodesk.Revit.DB CompoundStructureLayer](faece83a-6d49-41b0-2713-fe6cfaa5a3b5.htm)    
     The layer to be set.

#### Return Value

True if the layer is internally consistent, false if the layer is not internally consistent.

# Remarks

If the layer function is not Membrane or StructuralDeck, the width must be greater than zero. If the layer function is not StructuralDeck, then the deck embedding type must be Invalid, and the deck profile id must be InvalidElementId.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)