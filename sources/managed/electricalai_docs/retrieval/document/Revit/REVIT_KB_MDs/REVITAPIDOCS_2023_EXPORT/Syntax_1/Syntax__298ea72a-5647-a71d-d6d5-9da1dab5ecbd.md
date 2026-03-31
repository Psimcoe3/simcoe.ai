[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddDistributionSysType Method

---



|  |
| --- |
| [ElectricalSetting Class](d0c5bb12-7cf7-35e0-fc72-51e491c56bc2.htm)   [See Also](#seeAlsoToggle) |

Add a new distribution system type to project.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public DistributionSysType AddDistributionSysType( 	string name, 	ElectricalPhase phase, 	ElectricalPhaseConfiguration phaseConfig, 	int numWire, 	VoltageType volLineToLine, 	VoltageType volLineToGround ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function AddDistributionSysType ( _ 	name As String, _ 	phase As ElectricalPhase, _ 	phaseConfig As ElectricalPhaseConfiguration, _ 	numWire As Integer, _ 	volLineToLine As VoltageType, _ 	volLineToGround As VoltageType _ ) As DistributionSysType ``` |

 

| Visual C++ |
| --- |
| ``` public: DistributionSysType^ AddDistributionSysType( 	String^ name,  	ElectricalPhase phase,  	ElectricalPhaseConfiguration phaseConfig,  	int numWire,  	VoltageType^ volLineToLine,  	VoltageType^ volLineToGround ) ``` |

#### Parameters

name
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)    
     The name of new added distribution system type

phase
:   Type:  [Autodesk.Revit.DB.Electrical ElectricalPhase](aff8cc61-d006-c2df-8687-86c41f219384.htm)    
     Single or three phase this type is

phaseConfig
:   Type:  [Autodesk.Revit.DB.Electrical ElectricalPhaseConfiguration](fa91ef24-f277-a8b8-822c-7ec5fc076035.htm)    
     Configuration property of given phase

numWire
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     Wire number of this distribution system

volLineToLine
:   Type:  [Autodesk.Revit.DB.Electrical VoltageType](6b462685-b825-f8f9-f218-035107f7aaf0.htm)    
     Type of line to line voltage in this system

volLineToGround
:   Type:  [Autodesk.Revit.DB.Electrical VoltageType](6b462685-b825-f8f9-f218-035107f7aaf0.htm)    
     Type of line to ground voltage in this system

#### Return Value

New added distribution system type object.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The name can't be    a null reference (  Nothing  in Visual Basic)  , empty string, or equal with any existing one, phaseConfig should be defined and numWire can only be 3 or 4 in case of three phase, numWire can only be 2 or 3 in case of single phase, otherwise exception will be thrown. |

# See Also

[ElectricalSetting Class](d0c5bb12-7cf7-35e0-fc72-51e491c56bc2.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)