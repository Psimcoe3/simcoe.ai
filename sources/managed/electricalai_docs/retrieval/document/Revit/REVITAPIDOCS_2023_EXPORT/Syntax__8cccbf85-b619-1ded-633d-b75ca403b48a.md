[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Direction Property

---



|  |
| --- |
| [ReferencePlane Class](e7003ec7-1dbe-50a2-fb3d-a83a5a3b5b9f.htm)   [See Also](#seeAlsoToggle) |

The direction of the reference plane.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public XYZ Direction { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Direction As XYZ 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property XYZ^ Direction { 	XYZ^ get (); 	void set (XYZ^ value); } ``` |

# Remarks

When setting this property, an exception will be thrown if the direction vector is not perpendicular to the normal vector.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: newDir has zero length. |

# See Also

[ReferencePlane Class](e7003ec7-1dbe-50a2-fb3d-a83a5a3b5b9f.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)