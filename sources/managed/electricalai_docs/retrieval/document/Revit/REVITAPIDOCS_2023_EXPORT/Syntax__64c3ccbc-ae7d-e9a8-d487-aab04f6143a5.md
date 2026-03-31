[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method

---



|  |
| --- |
| [CurveUV Class](2d1d9c1f-afb6-fc09-f461-54cf0d511bf0.htm)   [See Also](#seeAlsoToggle) |

Create a CurveUV from a bounded 3D Curve lying in the XY plane.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static CurveUV Create( 	Curve curve3D ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	curve3D As Curve _ ) As CurveUV ``` |

 

| Visual C++ |
| --- |
| ``` public: static CurveUV^ Create( 	Curve^ curve3D ) ``` |

#### Parameters

curve3D
:   Type:  [Autodesk.Revit.DB Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)    
     The input bounded 3D Curve lying in the XY plane (i.e., z = 0 everywhere along the curve).

#### Return Value

The newly created CurveUV.

# Remarks

The XY plane is identified with the uv parameter space of the surface to which this SurfParamSpaceCurve refers.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The input Curve is not a bounded 3D Curve lying in the XY plane (i.e., z = 0 everywhere along the curve). |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[CurveUV Class](2d1d9c1f-afb6-fc09-f461-54cf0d511bf0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)