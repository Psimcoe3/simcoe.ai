[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsPipingConnector Method

---



|  |
| --- |
| [Pipe Class](aa1b8294-c12d-ece0-00af-b17c1f1c9e03.htm)   [See Also](#seeAlsoToggle) |

Checks if the given connector is a valid piping connector.

**Namespace:**   [Autodesk.Revit.DB.Plumbing](cc553597-37c2-fcd9-6025-d904c129c80a.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public static bool IsPipingConnector( 	Connector connector ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsPipingConnector ( _ 	connector As Connector _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsPipingConnector( 	Connector^ connector ) ``` |

#### Parameters

connector
:   Type:  [Autodesk.Revit.DB Connector](11e07082-b3f2-26a1-de79-16535f44716c.htm)    
     Connector to check

#### Return Value

True if the connector has the Piping domain type.

# Remarks

A connector must be Piping domain type to be connected with other pipes.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[Pipe Class](aa1b8294-c12d-ece0-00af-b17c1f1c9e03.htm)

[Autodesk.Revit.DB.Plumbing Namespace](cc553597-37c2-fcd9-6025-d904c129c80a.htm)