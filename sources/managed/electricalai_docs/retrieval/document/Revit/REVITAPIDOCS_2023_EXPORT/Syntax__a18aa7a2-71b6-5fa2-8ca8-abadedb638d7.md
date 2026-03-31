[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateByThreePoints Method

---



|  |
| --- |
| [Plane Class](6a6ee978-f114-558d-3c69-00d289aa855f.htm)   [See Also](#seeAlsoToggle) |

Creates a Plane object passing through three points supplied as arguments.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public static Plane CreateByThreePoints( 	XYZ point1, 	XYZ point2, 	XYZ point3 ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateByThreePoints ( _ 	point1 As XYZ, _ 	point2 As XYZ, _ 	point3 As XYZ _ ) As Plane ``` |

 

| Visual C++ |
| --- |
| ``` public: static Plane^ CreateByThreePoints( 	XYZ^ point1,  	XYZ^ point2,  	XYZ^ point3 ) ``` |

#### Parameters

point1
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     First of the three points that define a unique plane. The created Plane object will pass through these points.

point2
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     Second of the three points that define a unique plane.

point3
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     Third of the three points that define a unique plane.

# Remarks

The points supplied as arguments must fully define a plane: they may not lie on a straight line or be too close to each other. The points must lie within the Revit design limits. This function does not guarantee a specific parameterization of the created Plane. Use Plane.Create(Frame) to enforce a specific parameterization of the created Plane object. All three points are expected to lie within the Revit design limits  [IsWithinLengthLimits(XYZ)](ac2171af-4250-8a30-faa7-4d7030d29a03.htm)  .

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The input point lies outside of Revit design limits. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentsInconsistentException](05972c68-fa6d-3a83-d720-ad84fbc4780f.htm) | Throws if the input points do not define a unique plane. This is typically caused by points being too close to each other, or all three points being on or close to a straight line. |

# See Also

[Plane Class](6a6ee978-f114-558d-3c69-00d289aa855f.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)