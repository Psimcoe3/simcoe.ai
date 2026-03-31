[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CoordinateSystem Property

---



|  |
| --- |
| [Connector Class](11e07082-b3f2-26a1-de79-16535f44716c.htm)   [See Also](#seeAlsoToggle) |

The coordinate system of the connector.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual Transform CoordinateSystem { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable ReadOnly Property CoordinateSystem As Transform 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual property Transform^ CoordinateSystem { 	Transform^ get (); } ``` |

#### Implements

 [IConnector CoordinateSystem](83c23e11-64cf-0d4c-1233-d90f69c7de8e.htm)

# Remarks

The coordinate system's origin is the location of the connector and the Z-axis is normal to the connector.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when the connector is of logical type. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown on failure to get coordinate system. |

# See Also

[Connector Class](11e07082-b3f2-26a1-de79-16535f44716c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)