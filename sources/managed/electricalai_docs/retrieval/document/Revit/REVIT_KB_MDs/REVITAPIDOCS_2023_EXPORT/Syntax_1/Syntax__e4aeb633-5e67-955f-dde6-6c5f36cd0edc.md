[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NewWires Method

---



|  |
| --- |
| [ElectricalSystem Class](158b4be3-bbe5-11eb-cccc-788edd3a7590.htm)   [See Also](#seeAlsoToggle) |

Create a bunch of wires for the electrical system.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public WireSet NewWires( 	View view, 	WiringType wiringType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function NewWires ( _ 	view As View, _ 	wiringType As WiringType _ ) As WireSet ``` |

 

| Visual C++ |
| --- |
| ``` public: WireSet^ NewWires( 	View^ view,  	WiringType wiringType ) ``` |

#### Parameters

view
:   Type:  [Autodesk.Revit.DB View](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)    
     The view in which the wire is to be visible.

wiringType
:   Type:  [Autodesk.Revit.DB.Electrical WiringType](fb484864-f9d0-7335-1f91-d7ac587f15fb.htm)    
     Specify the wiring type (Arc or Chamfer) that is to be applied to all newly created wires.

#### Return Value

New created wires

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | This method can only be used to create a bunch of wires according to specific pairs of elements, so if there exists a    a null reference (  Nothing  in Visual Basic)  element in any pair of familyInstancePairs, the exception will be thrown. |

# See Also

[ElectricalSystem Class](158b4be3-bbe5-11eb-cccc-788edd3a7590.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)