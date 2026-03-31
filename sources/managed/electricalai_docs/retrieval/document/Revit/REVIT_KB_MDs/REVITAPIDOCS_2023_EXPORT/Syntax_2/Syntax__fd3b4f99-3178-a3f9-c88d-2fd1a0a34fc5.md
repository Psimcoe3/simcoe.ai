[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AppendVertex Method

---



|  |
| --- |
| [Wire Class](c2acf13b-0d8b-8415-9682-ae64eb5e5895.htm)   [See Also](#seeAlsoToggle) |

Appends one vertex to the end of the wire.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public void AppendVertex( 	XYZ vertexPoint ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub AppendVertex ( _ 	vertexPoint As XYZ _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void AppendVertex( 	XYZ^ vertexPoint ) ``` |

#### Parameters

vertexPoint
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The vertex to be appended.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The vertex point cannot be added to the wire because there is already a vertex at this position on the view plane (within tolerance). |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Mechanical Electrical Piping. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The end point is already connected to an element, so a new endpoint vertex cannot be appended. |

# See Also

[Wire Class](c2acf13b-0d8b-8415-9682-ae64eb5e5895.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)