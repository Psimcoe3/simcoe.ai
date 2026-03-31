[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidProfileCurve Method (Frame, Curve)

---



|  |
| --- |
| [RevolvedSurface Class](ce0b47e0-2b24-61f5-1434-87fe3ff70390.htm)   [See Also](#seeAlsoToggle) |

Checks if the input profile curve is valid to create a surface of revolution in the given frame of reference.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public static bool IsValidProfileCurve( 	Frame frameOfReference, 	Curve profileCurve ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsValidProfileCurve ( _ 	frameOfReference As Frame, _ 	profileCurve As Curve _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsValidProfileCurve( 	Frame^ frameOfReference,  	Curve^ profileCurve ) ``` |

#### Parameters

frameOfReference
:   Type:  [Autodesk.Revit.DB Frame](d44b3fd1-34d0-bfd0-55f6-de24235edf2e.htm)    
     frameOfReference is an orthonormal frame that defines a local coordinate system for the surface of revolution.

    * The frame can be "right-handed" or "left-handed".
    * The origin of the frame is the base of point of the axis of revolution.
    * The BasisZ of the frame is the direction of the axis.

profileCurve
:   Type:  [Autodesk.Revit.DB Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)    
     The profile curve.

#### Return Value

True if the profile curve is valid; False otherwise.

# Remarks

The validity is defined as follows:

* The profile curve is bounded and non-degenerate.
* It is co-planar with the axis of revolution.
* It lies on the xz plane of the frame.
* It lies on the right side of the axis.
* Only the end points of the profile curve can touch the axis.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[RevolvedSurface Class](ce0b47e0-2b24-61f5-1434-87fe3ff70390.htm)

[IsValidProfileCurve Overload](b4ba507e-b41c-19a4-944c-4ad9b47e400e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)