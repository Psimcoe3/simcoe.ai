[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidCircuitNamingSchemeId Method

---



|  |
| --- |
| [CircuitNamingSchemeSettings Class](60f49706-88f3-d2fb-0732-b1536c6e2e82.htm)   [See Also](#seeAlsoToggle) |

Verifies that the circuit naming scheme id can be used with CircuitNamingSchemeSettings.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static bool IsValidCircuitNamingSchemeId( 	Document aDocument, 	ElementId circuitNamingSchemeId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsValidCircuitNamingSchemeId ( _ 	aDocument As Document, _ 	circuitNamingSchemeId As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsValidCircuitNamingSchemeId( 	Document^ aDocument,  	ElementId^ circuitNamingSchemeId ) ``` |

#### Parameters

aDocument
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

circuitNamingSchemeId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The circuit naming scheme id to be checked.

#### Return Value

True if the circuit naming scheme id is valid for CircuitNamingSchemeSettings.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[CircuitNamingSchemeSettings Class](60f49706-88f3-d2fb-0732-b1536c6e2e82.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)