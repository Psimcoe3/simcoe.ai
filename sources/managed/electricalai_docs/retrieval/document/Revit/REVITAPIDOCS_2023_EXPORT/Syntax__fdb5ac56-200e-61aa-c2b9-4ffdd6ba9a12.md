[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetCircuitNamingSchemeSettings Method

---



|  |
| --- |
| [CircuitNamingSchemeSettings Class](60f49706-88f3-d2fb-0732-b1536c6e2e82.htm)   [See Also](#seeAlsoToggle) |

Gets the circuit naming scheme settings of the project.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static CircuitNamingSchemeSettings GetCircuitNamingSchemeSettings( 	Document cda ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetCircuitNamingSchemeSettings ( _ 	cda As Document _ ) As CircuitNamingSchemeSettings ``` |

 

| Visual C++ |
| --- |
| ``` public: static CircuitNamingSchemeSettings^ GetCircuitNamingSchemeSettings( 	Document^ cda ) ``` |

#### Parameters

cda
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

#### Return Value

The circuit naming scheme settings of the project.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[CircuitNamingSchemeSettings Class](60f49706-88f3-d2fb-0732-b1536c6e2e82.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)