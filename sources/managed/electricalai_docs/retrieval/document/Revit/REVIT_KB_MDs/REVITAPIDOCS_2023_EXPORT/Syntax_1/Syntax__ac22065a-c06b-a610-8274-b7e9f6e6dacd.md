[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetGridSegmentReference Method

---



|  |
| --- |
| [DividedSurface Class](782e1ac7-4e74-9a32-6b03-0a20f7d55217.htm)   [See Also](#seeAlsoToggle) |

Get a reference to a line segment connecting two adjacent grid nodes.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public Reference GetGridSegmentReference( 	GridNode gridNode, 	GridSegmentDirection gridSegmentDirection ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetGridSegmentReference ( _ 	gridNode As GridNode, _ 	gridSegmentDirection As GridSegmentDirection _ ) As Reference ``` |

 

| Visual C++ |
| --- |
| ``` public: Reference^ GetGridSegmentReference( 	GridNode gridNode,  	GridSegmentDirection gridSegmentDirection ) ``` |

#### Parameters

gridNode
:   Type:  [Autodesk.Revit.DB GridNode](231a5e2c-a18a-7710-a514-b320c4a2cc70.htm)

gridSegmentDirection
:   Type:  [Autodesk.Revit.DB GridSegmentDirection](d092a487-df66-fa3f-bfef-7d11003ecb8c.htm)

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | Thrown when the grid node indexes are outside the range [ 0, NumberOfUGridlines - 1 ], [ 0, NumberOfVGridlines - 1 ], or when the adjacent grid node specified by gridSegmentDirection is out of range. |

# See Also

[DividedSurface Class](782e1ac7-4e74-9a32-6b03-0a20f7d55217.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)