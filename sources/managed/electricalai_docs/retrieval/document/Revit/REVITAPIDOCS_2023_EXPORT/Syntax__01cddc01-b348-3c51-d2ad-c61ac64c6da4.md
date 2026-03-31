[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateRotation Method

---



|  |
| --- |
| [Transform Class](58dd01c8-b3fc-7142-e4f3-c524079a282d.htm)   [See Also](#seeAlsoToggle) |

Creates a transform that represents a rotation about the given axis at (0, 0, 0).

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public static Transform CreateRotation( 	XYZ axis, 	double angle ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateRotation ( _ 	axis As XYZ, _ 	angle As Double _ ) As Transform ``` |

 

| Visual C++ |
| --- |
| ``` public: static Transform^ CreateRotation( 	XYZ^ axis,  	double angle ) ``` |

#### Parameters

axis
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The rotation axis.

angle
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The angle.

#### Return Value

The new transform.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given value for angle is not finite |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was NULL |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | axis has zero length. |

# See Also

[Transform Class](58dd01c8-b3fc-7142-e4f3-c524079a282d.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)