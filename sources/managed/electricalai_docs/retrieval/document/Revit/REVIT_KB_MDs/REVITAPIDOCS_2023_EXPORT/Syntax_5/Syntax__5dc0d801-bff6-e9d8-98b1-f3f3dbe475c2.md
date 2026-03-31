[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method (Curve, XYZ)

---



|  |
| --- |
| [RuledSurface Class](9a33fec9-bbcd-f035-3194-cf36122b6cc6.htm)   [See Also](#seeAlsoToggle) |

Creates a Surface object coincident with the ruled surface joining a bounded generating curve to a point.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public static Surface Create( 	Curve profileCurve, 	XYZ point ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	profileCurve As Curve, _ 	point As XYZ _ ) As Surface ``` |

 

| Visual C++ |
| --- |
| ``` public: static Surface^ Create( 	Curve^ profileCurve,  	XYZ^ point ) ``` |

#### Parameters

profileCurve
:   Type:  [Autodesk.Revit.DB Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)    
     The profile curve; must be bounded and non-degenerate.

point
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The point. Expected to lie within the Revit design limits  [IsWithinLengthLimits(XYZ)](ac2171af-4250-8a30-faa7-4d7030d29a03.htm)  .

#### Return Value

The created surface. Note that this surface may not be of type RuledSurf.

# Remarks

The returned surface may not be of type RuledSurf - this function will create a surface of the simplest possible type (Plane, CylindricalSurface, etc.) that can be used to represent the given ruled surface. Given that the surface may be simplified, this function does not guarantee any particular parameterization of the surface.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The input profileCurve is not bound. -or- The profileCurve is degenerate (its length is too close to zero). -or- The input point lies outside of Revit design limits. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[RuledSurface Class](9a33fec9-bbcd-f035-3194-cf36122b6cc6.htm)

[Create Overload](91a664ea-0aeb-d748-8a2d-8b8c1bb62cb1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)