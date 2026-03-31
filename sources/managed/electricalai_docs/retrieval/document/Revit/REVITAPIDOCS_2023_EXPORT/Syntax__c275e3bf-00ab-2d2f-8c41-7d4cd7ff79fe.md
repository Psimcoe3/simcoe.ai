[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetLocation Method

---



|  |
| --- |
| [ImageInstance Class](ff77d6c8-a94a-067a-cd95-4f2cd3ec8dcc.htm)   [See Also](#seeAlsoToggle) |

Returns the location of one of the points of the ImageInstance

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2020

# Syntax

| C# |
| --- |
| ``` public XYZ GetLocation( 	BoxPlacement placementPoint ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetLocation ( _ 	placementPoint As BoxPlacement _ ) As XYZ ``` |

 

| Visual C++ |
| --- |
| ``` public: XYZ^ GetLocation( 	BoxPlacement placementPoint ) ``` |

#### Parameters

placementPoint
:   Type:  [Autodesk.Revit.DB BoxPlacement](2ecf1f45-4890-8b9f-3de7-8d0eebeb7ce7.htm)    
     The placementPoint specifies for which point of the ImageInstance the location should be returned.

#### Return Value

The location of the specified point

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[ImageInstance Class](ff77d6c8-a94a-067a-cd95-4f2cd3ec8dcc.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)