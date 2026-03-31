[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ConnectTo Method

---



|  |
| --- |
| [Wire Class](c2acf13b-0d8b-8415-9682-ae64eb5e5895.htm)   [See Also](#seeAlsoToggle) |

Connects the wire to other elements.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public void ConnectTo( 	Connector startConnectorTo, 	Connector endConnectorTo ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub ConnectTo ( _ 	startConnectorTo As Connector, _ 	endConnectorTo As Connector _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void ConnectTo( 	Connector^ startConnectorTo,  	Connector^ endConnectorTo ) ``` |

#### Parameters

startConnectorTo
:   Type:  [Autodesk.Revit.DB Connector](11e07082-b3f2-26a1-de79-16535f44716c.htm)    
     The connector that the start connector of the wire connects to.

endConnectorTo
:   Type:  [Autodesk.Revit.DB Connector](11e07082-b3f2-26a1-de79-16535f44716c.htm)    
     The connector that the end connector of the wire connects to.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | startConnectorTo cannot be connected to a wire, as it is not an electrical connector. -or- endConnectorTo cannot be connected to a wire, as it is not an electrical connector. -or- startConnectorTo or/and endConnectorTo cannot be connected to a wire, as wire can't connect both connectors to same wire or same connector. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Cannot connect the wire to the start connector or the end connector. |

# See Also

[Wire Class](c2acf13b-0d8b-8415-9682-ae64eb5e5895.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)