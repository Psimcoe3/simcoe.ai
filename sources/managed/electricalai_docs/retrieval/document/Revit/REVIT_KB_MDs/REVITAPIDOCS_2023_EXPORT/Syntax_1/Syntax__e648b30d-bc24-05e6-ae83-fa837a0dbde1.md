[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AssignedFlowFactor Property

---



|  |
| --- |
| [Connector Class](11e07082-b3f2-26a1-de79-16535f44716c.htm)   [See Also](#seeAlsoToggle) |

The assigned flow factor of this connector.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public double AssignedFlowFactor { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property AssignedFlowFactor As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double AssignedFlowFactor { 	double get (); 	void set (double value); } ``` |

# Remarks

Assigned flow factor may be assigned for connectors of some family instances. In order to set this property, it must be mapped to a writable instance parameter in the family definition.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when get assigned flow factor from a connector not in family instance. Thrown when the connector's domain is not DomainHvac or DomainPiping. |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Throw when set an invalid value. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown on failure to get or set assigned flow factor. |

# See Also

[Connector Class](11e07082-b3f2-26a1-de79-16535f44716c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)