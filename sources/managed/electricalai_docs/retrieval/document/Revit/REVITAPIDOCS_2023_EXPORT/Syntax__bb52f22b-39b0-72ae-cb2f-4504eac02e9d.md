[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetDeckEmbeddingType Method

---



|  |
| --- |
| [CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.htm)   [See Also](#seeAlsoToggle) |

Retrieves the deck embedding type used for the specified structural deck.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public StructDeckEmbeddingType GetDeckEmbeddingType( 	int layerIdx ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetDeckEmbeddingType ( _ 	layerIdx As Integer _ ) As StructDeckEmbeddingType ``` |

 

| Visual C++ |
| --- |
| ``` public: StructDeckEmbeddingType GetDeckEmbeddingType( 	int layerIdx ) ``` |

#### Parameters

layerIdx
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     Index of a layer in the CompoundStructure.

#### Return Value

The embedding type of the structural deck associated to the specified layer. Invalid if it is not a structural deck.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The layer index is out of range. |

# See Also

[CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)