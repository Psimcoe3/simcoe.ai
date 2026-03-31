[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method (Connector, ElectricalSystemType)

---



|  |
| --- |
| [ElectricalSystem Class](158b4be3-bbe5-11eb-cccc-788edd3a7590.htm)   [See Also](#seeAlsoToggle) |

Creates a new MEP Electrical System element from an unused Connector.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public static ElectricalSystem Create( 	Connector connector, 	ElectricalSystemType elecSysType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	connector As Connector, _ 	elecSysType As ElectricalSystemType _ ) As ElectricalSystem ``` |

 

| Visual C++ |
| --- |
| ``` public: static ElectricalSystem^ Create( 	Connector^ connector,  	ElectricalSystemType elecSysType ) ``` |

#### Parameters

connector
:   Type:  [Autodesk.Revit.DB Connector](11e07082-b3f2-26a1-de79-16535f44716c.htm)    
     The Connector to create this Electrical System.

elecSysType
:   Type:  [Autodesk.Revit.DB.Electrical ElectricalSystemType](90f62108-9cd1-a66a-a123-8372307f4e7f.htm)    
     The System Type of electrical system.

#### Return Value

If successful a new MEP Electrical System element within the project, otherwise    a null reference (  Nothing  in Visual Basic)  .

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Mechanical Electrical Piping. |

# See Also

[ElectricalSystem Class](158b4be3-bbe5-11eb-cccc-788edd3a7590.htm)

[Create Overload](b3ea7251-7230-ac0a-d5cc-0806b0c0ec1e.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)