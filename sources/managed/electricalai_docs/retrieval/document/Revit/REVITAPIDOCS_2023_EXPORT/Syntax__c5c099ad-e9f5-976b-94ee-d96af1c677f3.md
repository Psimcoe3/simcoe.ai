[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CrossProduct Method

---



|  |
| --- |
| [XYZ Class](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)   [See Also](#seeAlsoToggle) |

The cross product of this vector and the specified vector.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public XYZ CrossProduct( 	XYZ source ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function CrossProduct ( _ 	source As XYZ _ ) As XYZ ``` |

 

| Visual C++ |
| --- |
| ``` public: XYZ^ CrossProduct( 	XYZ^ source ) ``` |

#### Parameters

source
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The vector to multiply with this vector.

#### Return Value

The vector equal to the cross product.

# Remarks

The cross product is defined as the vector which is perpendicular to both vectors with a magnitude equal to the area of the parallelogram they span. Also known as vector product or outer product.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when source is    a null reference (  Nothing  in Visual Basic)  . |

# See Also

[XYZ Class](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)