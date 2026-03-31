[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CanAdjustEndLength Method

---



|  |
| --- |
| [FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.htm)   [See Also](#seeAlsoToggle) |

Checks if the end of fabrication part can be adjusted.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public bool CanAdjustEndLength( 	Connector partConn ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function CanAdjustEndLength ( _ 	partConn As Connector _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool CanAdjustEndLength( 	Connector^ partConn ) ``` |

#### Parameters

partConn
:   Type:  [Autodesk.Revit.DB Connector](11e07082-b3f2-26a1-de79-16535f44716c.htm)    
     # The connector of the fabrication part to adjust length.

#### Return Value

True if the end of fabrication part can be adjusted.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)