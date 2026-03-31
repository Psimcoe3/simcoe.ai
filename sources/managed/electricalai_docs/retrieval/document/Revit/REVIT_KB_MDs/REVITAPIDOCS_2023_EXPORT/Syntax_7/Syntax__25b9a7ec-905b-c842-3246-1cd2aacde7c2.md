[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DoubleWallConnectorId Property

---



|  |
| --- |
| [FabricationConnectorInfo Class](5da97d87-a3f6-f239-3c5c-102d2d82f942.htm)   [See Also](#seeAlsoToggle) |

Fabrication double wall connector Id.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public int DoubleWallConnectorId { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property DoubleWallConnectorId As Integer 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property int DoubleWallConnectorId { 	int get (); 	void set (int value); } ``` |

# Remarks

A reference to the fabrication configuration connectors. Setting the connector value will also set the connector lock. A value of 0 indicates no connector.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: doubleWallConnectorId is invalid based on the shape and domain. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | No double wall connector available. -or- When setting this property: the connector cannot be modified on an owned fabrication part. -or- When setting this property: the connector is already connected. -or- When setting this property: the fabrication part is connected to more than one item. |

# See Also

[FabricationConnectorInfo Class](5da97d87-a3f6-f239-3c5c-102d2d82f942.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)