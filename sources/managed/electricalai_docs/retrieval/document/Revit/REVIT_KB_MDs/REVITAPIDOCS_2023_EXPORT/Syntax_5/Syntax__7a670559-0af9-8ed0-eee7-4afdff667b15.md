[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WiringType Property

---



|  |
| --- |
| [Wire Class](c2acf13b-0d8b-8415-9682-ae64eb5e5895.htm)   [See Also](#seeAlsoToggle) |

The wiring type(arc or chamfer) for the wire.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public WiringType WiringType { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property WiringType As WiringType 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property WiringType WiringType { 	WiringType get (); 	void set (WiringType value); } ``` |

# Remarks

If the WiringType is arc, the shape of the wire depends on the number of points - it may be linear, a circular arc, or a spline.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[Wire Class](c2acf13b-0d8b-8415-9682-ae64eb5e5895.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)