[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ConnectTo Method

---



|  |
| --- |
| [Connector Class](11e07082-b3f2-26a1-de79-16535f44716c.htm)   [See Also](#seeAlsoToggle) |

Make connection between two connectors.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public void ConnectTo( 	Connector connector ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub ConnectTo ( _ 	connector As Connector _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void ConnectTo( 	Connector^ connector ) ``` |

#### Parameters

connector
:   Type:  [Autodesk.Revit.DB Connector](11e07082-b3f2-26a1-de79-16535f44716c.htm)    
     Indicate the connector will be connected to.

# Remarks

Connection success may create a new Fitting between two connectors, if necessary.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when argument is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Argument is invalid. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when two connectors with different domain types. Thrown when these two connectors fail to connect each other. Thrown when connection already exists. |

# See Also

[Connector Class](11e07082-b3f2-26a1-de79-16535f44716c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)