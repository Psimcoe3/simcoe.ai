[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AdjustEndLength Method

---



|  |
| --- |
| [FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.htm)   [See Also](#seeAlsoToggle) |

Adjusts the length for the specified connector.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public double AdjustEndLength( 	Connector partConn, 	double lengthToAdjust, 	bool totalLengthOnly ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function AdjustEndLength ( _ 	partConn As Connector, _ 	lengthToAdjust As Double, _ 	totalLengthOnly As Boolean _ ) As Double ``` |

 

| Visual C++ |
| --- |
| ``` public: double AdjustEndLength( 	Connector^ partConn,  	double lengthToAdjust,  	bool totalLengthOnly ) ``` |

#### Parameters

partConn
:   Type:  [Autodesk.Revit.DB Connector](11e07082-b3f2-26a1-de79-16535f44716c.htm)    
     # The connector of the fabrication part to adjust length.

lengthToAdjust
:   Type:  System Double    
     The length to adjust.

totalLengthOnly
:   Type:  System Boolean    
     True if adjust the total length only when adjust length.

#### Return Value

The adjusted length.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The end of the fabrication part of the connector can not be adjusted. -or- Connector is connected. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)