[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CircuitNamingSchemeId Property

---



|  |
| --- |
| [ElectricalEquipment Class](a93a0589-784b-27a3-c7d0-1122921a7a23.htm)   [See Also](#seeAlsoToggle) |

The CircuitNamingSchemeId used in the Electrical Equipment. The CircuitNamingSchemeId is used to retrieve the circuit naming scheme id of the Electrical Equipment.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public ElementId CircuitNamingSchemeId { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property CircuitNamingSchemeId As ElementId 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ CircuitNamingSchemeId { 	ElementId^ get (); 	void set (ElementId^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The circuit naming scheme id is invalid for the Electrical Equipment. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[ElectricalEquipment Class](a93a0589-784b-27a3-c7d0-1122921a7a23.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)