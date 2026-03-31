[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AssignedFixtureUnits Property

---



|  |
| --- |
| [Connector Class](11e07082-b3f2-26a1-de79-16535f44716c.htm)   [See Also](#seeAlsoToggle) |

The assigned fixture units of the connector.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public double AssignedFixtureUnits { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property AssignedFixtureUnits As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double AssignedFixtureUnits { 	double get (); 	void set (double value); } ``` |

# Remarks

Assigned fixture units may be assigned for connectors of some family instances.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when the connector's domain is not DomainPiping. Thrown when the connector is not in a family instance. |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when set an invalid value. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown on failure to get or set assigned fixture units. |

# See Also

[Connector Class](11e07082-b3f2-26a1-de79-16535f44716c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)