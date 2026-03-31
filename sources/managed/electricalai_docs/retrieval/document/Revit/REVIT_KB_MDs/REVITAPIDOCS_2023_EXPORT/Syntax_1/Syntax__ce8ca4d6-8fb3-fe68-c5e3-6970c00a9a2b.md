[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NewPipingSystem Method

---



|  |
| --- |
| [Document Class](ab1718f9-45fb-b3d3-827e-32ff81cf929c.htm)   [See Also](#seeAlsoToggle) |

Creates a new MEP piping system element.

**Namespace:**   [Autodesk.Revit.Creation](ded320da-058a-4edd-0418-0582389559a7.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public PipingSystem NewPipingSystem( 	Connector baseEquipmentConnector, 	ConnectorSet connectors, 	PipeSystemType pipingSystemType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function NewPipingSystem ( _ 	baseEquipmentConnector As Connector, _ 	connectors As ConnectorSet, _ 	pipingSystemType As PipeSystemType _ ) As PipingSystem ``` |

 

| Visual C++ |
| --- |
| ``` public: PipingSystem^ NewPipingSystem( 	Connector^ baseEquipmentConnector,  	ConnectorSet^ connectors,  	PipeSystemType pipingSystemType ) ``` |

#### Parameters

baseEquipmentConnector
:   Type:  [Autodesk.Revit.DB Connector](11e07082-b3f2-26a1-de79-16535f44716c.htm)    
     One connector within base equipment which is used to connect with the system. The base equipment is optional for the system, so this argument may be    a null reference (  Nothing  in Visual Basic)  . The baseEquipmentConnector should not be included in the connectors.

connectors
:   Type:  [Autodesk.Revit.DB ConnectorSet](a9821fc1-54cf-5f69-13a9-25d506ecb048.htm)    
     Connectors that will connect to the system. The owner elements of these connectors will be added into system as its elements.

pipingSystemType
:   Type:  [Autodesk.Revit.DB.Plumbing PipeSystemType](24165d09-9267-54b7-3e32-6405d1343c2e.htm)    
     The System type.

#### Return Value

If creation was successful then an instance of piping system is returned, otherwise an exception with information will be thrown.

# Remarks

This method will regenerate the document even in manual regeneration mode.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when calling this function outside of the Autodesk Revit MEP product. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the connectors parameter value is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | Thrown when the pipingSystemType parameter value is out of permitted scope. |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when some connectors can't be used to create the mechanical system. All the input connectors and base equipment connector should match system type and domain with the system, and they should not have been used in another system. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when the piping system creation failed. |

# See Also

[Document Class](ab1718f9-45fb-b3d3-827e-32ff81cf929c.htm)

[Autodesk.Revit.Creation Namespace](ded320da-058a-4edd-0418-0582389559a7.htm)