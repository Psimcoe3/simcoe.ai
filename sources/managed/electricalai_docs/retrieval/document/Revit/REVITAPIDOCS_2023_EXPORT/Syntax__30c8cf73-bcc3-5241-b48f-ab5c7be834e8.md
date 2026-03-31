[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetGridNodeUV Method

---



|  |
| --- |
| [DividedSurface Class](782e1ac7-4e74-9a32-6b03-0a20f7d55217.htm)   [See Also](#seeAlsoToggle) |

Get the position of a grid node in UV coordinates in the surface.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public UV GetGridNodeUV( 	GridNode gridNode ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetGridNodeUV ( _ 	gridNode As GridNode _ ) As UV ``` |

 

| Visual C++ |
| --- |
| ``` public: UV^ GetGridNodeUV( 	GridNode gridNode ) ``` |

#### Parameters

gridNode
:   Type:  [Autodesk.Revit.DB GridNode](231a5e2c-a18a-7710-a514-b320c4a2cc70.htm)

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | Thrown when the grid node indexes are outside the range [ 0, NumberOfUGridlines - 1 ], [ 0, NumberOfVGridlines - 1 ]. |

# See Also

[DividedSurface Class](782e1ac7-4e74-9a32-6b03-0a20f7d55217.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)