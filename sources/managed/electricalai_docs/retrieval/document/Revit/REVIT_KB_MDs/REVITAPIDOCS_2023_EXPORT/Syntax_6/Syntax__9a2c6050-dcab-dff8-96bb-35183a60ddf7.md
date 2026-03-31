[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CanConnectToUpstreamNode Method

---



|  |
| --- |
| [ElectricalAnalyticalNode Class](562d1f7d-c9df-bee5-4659-4f8607ee4333.htm)   [See Also](#seeAlsoToggle) |

Verifies that the current node can connect to the upstream node.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public bool CanConnectToUpstreamNode( 	ElementId upstreamNodeId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function CanConnectToUpstreamNode ( _ 	upstreamNodeId As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool CanConnectToUpstreamNode( 	ElementId^ upstreamNodeId ) ``` |

#### Parameters

upstreamNodeId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The upstream node id.

#### Return Value

True if the current node can connect to the upstream node.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The analytical distribution node is full of downstream nodes. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The analytical distribution node is full of upstream nodes. |

# See Also

[ElectricalAnalyticalNode Class](562d1f7d-c9df-bee5-4659-4f8607ee4333.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)