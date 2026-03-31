[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WireType Property

---



|  |
| --- |
| [ElectricalSystem Class](158b4be3-bbe5-11eb-cccc-788edd3a7590.htm)   [See Also](#seeAlsoToggle) |

The wire type of the Electrical System.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public WireType WireType { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property WireType As WireType 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property WireType^ WireType { 	WireType^ get (); 	void set (WireType^ value); } ``` |

# Remarks

This property is used to retrieve the wire type of the Electrical System.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | When setting this property: None of the following disciplines is enabled: Mechanical Electrical Piping. |

# See Also

[ElectricalSystem Class](158b4be3-bbe5-11eb-cccc-788edd3a7590.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)