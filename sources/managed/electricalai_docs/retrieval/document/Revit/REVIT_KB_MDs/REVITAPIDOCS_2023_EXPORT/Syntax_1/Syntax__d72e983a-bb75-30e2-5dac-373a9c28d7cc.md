[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetMemberForces Method (Boolean, XYZ, XYZ)

---



|  |
| --- |
| [AnalyticalMember Class](57c87ac5-a82e-5c7e-2f06-6dbf1f697566.htm)   [See Also](#seeAlsoToggle) |

Sets Member Forces to Analytical Member.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public void SetMemberForces( 	bool start, 	XYZ force, 	XYZ moment ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetMemberForces ( _ 	start As Boolean, _ 	force As XYZ, _ 	moment As XYZ _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetMemberForces( 	bool start,  	XYZ^ force,  	XYZ^ moment ) ``` |

#### Parameters

start
:   Type:  System Boolean    
     Member Forces position on Analytical Member. True for start, false for end.

force
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The translational forces at specified position of the element. The x value of XYZ object represents force along x-axis of the Analytical Member coordinate system, y along y-axis, z along z-axis respectively.

moment
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The rotational forces at specified position of the element. The x value of XYZ object represents moment about x-axis of the Analytical Member coordinate system, y about y-axis, z about z-axis respectively.

# Remarks

If Analytical Member already have member forces defined for that end, newly provided values replace current one. Member forces are strictly related with releases. This means that setting member forces values is reasonable only for directions that have releases set to false.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[AnalyticalMember Class](57c87ac5-a82e-5c7e-2f06-6dbf1f697566.htm)

[SetMemberForces Overload](655c6acb-8742-2c1f-de00-460d086d1c13.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)