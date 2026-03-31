[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MomentVector2 Property

---



|  |
| --- |
| [LineLoad Class](ee5ec273-350a-1cdb-d136-0c454bb1446a.htm)   [See Also](#seeAlsoToggle) |

The moment vector applied to the end point of the line load, oriented according to OrientTo setting.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public XYZ MomentVector2 { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property MomentVector2 As XYZ 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property XYZ^ MomentVector2 { 	XYZ^ get (); 	void set (XYZ^ value); } ``` |

# Remarks

The default force unit is kN-m/m for metric, and kip-ft/ft for imperial. Use UnitUtils class methods to convert value from or to internal units.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[LineLoad Class](ee5ec273-350a-1cdb-d136-0c454bb1446a.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)