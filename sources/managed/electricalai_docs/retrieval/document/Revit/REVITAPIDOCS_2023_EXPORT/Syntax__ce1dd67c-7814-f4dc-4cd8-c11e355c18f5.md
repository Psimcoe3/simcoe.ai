[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MemberForces Constructor

---



|  |
| --- |
| [MemberForces Class](aecdc0e5-e656-64cc-c1be-73b34a5f5a15.htm)   [See Also](#seeAlsoToggle) |

Creates a new instance of MemberForces.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public MemberForces( 	bool start, 	XYZ force, 	XYZ moment ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	start As Boolean, _ 	force As XYZ, _ 	moment As XYZ _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: MemberForces( 	bool start,  	XYZ^ force,  	XYZ^ moment ) ``` |

#### Parameters

start
:   Type:  System Boolean    
     Member Forces position on analytical element. True for start, false for end.

force
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The Translational forces at specified position of the element. The x value of XYZ object represents force along x-axis of the analytical element coordinate system, y along y-axis, z along z-axis respectively.

moment
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The Rotational forces at specified position of the element. The x value of XYZ object represents moment about x-axis of the analytical element coordinate system, y about y-axis, z about z-axis respectively.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[MemberForces Class](aecdc0e5-e656-64cc-c1be-73b34a5f5a15.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)