[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsAlmostEqualTo Method (XYZ)

---



|  |
| --- |
| [XYZ Class](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)   [See Also](#seeAlsoToggle) |

Determines whether this vector and the specified vector are the same within the tolerance (1.0e-09).

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool IsAlmostEqualTo( 	XYZ source ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsAlmostEqualTo ( _ 	source As XYZ _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsAlmostEqualTo( 	XYZ^ source ) ``` |

#### Parameters

source
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The vector to compare with this vector.

#### Return Value

True if the vectors are the same; otherwise, false.

# Remarks

This routine uses Revit's default tolerance to compare two vectors to see if they are almost equivalent. Because the tolerance is small enough this can also be used to compare two points.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when source is    a null reference (  Nothing  in Visual Basic)  . |

# See Also

[XYZ Class](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)

[IsAlmostEqualTo Overload](dcad6f16-9898-2f6f-1325-5bae45de241a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)