[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Point Property

---



|  |
| --- |
| [PointLoad Class](3f703eb6-7eac-c80e-e693-ebcdd6b35bbe.htm)   [See Also](#seeAlsoToggle) |

Returns the position of point load, measured in decimal feet.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public XYZ Point { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Point As XYZ 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property XYZ^ Point { 	XYZ^ get (); 	void set (XYZ^ value); } ``` |

# Remarks

Loacation can be set only for non-hosted loads. To determine if load is hosted use  [IsHosted](76965c6d-473a-9ad9-8a72-baa7a47b055a.htm)  property.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[PointLoad Class](3f703eb6-7eac-c80e-e693-ebcdd6b35bbe.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)