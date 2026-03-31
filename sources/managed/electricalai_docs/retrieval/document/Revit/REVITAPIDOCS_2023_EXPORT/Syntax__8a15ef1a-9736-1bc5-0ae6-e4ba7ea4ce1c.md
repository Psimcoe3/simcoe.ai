[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AlignPartByConnectorToConnector Method

---



|  |
| --- |
| [FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.htm)   [See Also](#seeAlsoToggle) |

Align a part by its connector to another connector. This will replace the FabricationPart::AlignPartByConnectors method.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public static bool AlignPartByConnectorToConnector( 	Document document, 	Connector connector, 	Connector fixedConnector, 	double rotation, 	double slope, 	FabricationPartJustification justification ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function AlignPartByConnectorToConnector ( _ 	document As Document, _ 	connector As Connector, _ 	fixedConnector As Connector, _ 	rotation As Double, _ 	slope As Double, _ 	justification As FabricationPartJustification _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool AlignPartByConnectorToConnector( 	Document^ document,  	Connector^ connector,  	Connector^ fixedConnector,  	double rotation,  	double slope,  	FabricationPartJustification justification ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

connector
:   Type:  [Autodesk.Revit.DB Connector](11e07082-b3f2-26a1-de79-16535f44716c.htm)    
     The connector of the fabrication part to move by in free space.

fixedConnector
:   Type:  [Autodesk.Revit.DB Connector](11e07082-b3f2-26a1-de79-16535f44716c.htm)    
     The connector for the fabrication part or family connector to align to.

rotation
:   Type:  System Double    
     The rotation in radians.

slope
:   Type:  System Double    
     The slope value to flex to match if possible in fractional units (eg.1/50). Positive values are up, negative are down. Slopes can only be applied to fittings, whilst straights will inherit the slope from the piece it is connecting to.

justification
:   Type:  [Autodesk.Revit.DB.Fabrication FabricationPartJustification](5c6c9daf-4547-01f1-9ba8-39a970ca9e68.htm)    
     The justification to align eccentric parts.

#### Return Value

True if the alignment succeeds, false otherwise and the part will not move from the original position.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | For rectangular and oval parts the axis rotation must be a multiple of PI/2. -or- The connector does not belong to a fabrication part. -or- The fabrication part is connected. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)