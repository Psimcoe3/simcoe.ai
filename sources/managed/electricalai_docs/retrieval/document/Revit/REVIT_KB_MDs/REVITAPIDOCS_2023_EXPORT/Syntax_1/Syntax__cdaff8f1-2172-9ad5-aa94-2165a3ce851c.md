[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ElectricalSystemType Property

---



|  |
| --- |
| [Connector Class](11e07082-b3f2-26a1-de79-16535f44716c.htm)   [See Also](#seeAlsoToggle) |

The electrical system type of the connector.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public ElectricalSystemType ElectricalSystemType { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property ElectricalSystemType As ElectricalSystemType 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElectricalSystemType ElectricalSystemType { 	ElectricalSystemType get (); } ``` |

# Remarks

Instantaneous system type at this connector, calculated according to system. For unconnected connectors, system type is undefined.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when the connector's domain is not of DomainElectrical. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown on failure to get electrical system type. |

# See Also

[Connector Class](11e07082-b3f2-26a1-de79-16535f44716c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)