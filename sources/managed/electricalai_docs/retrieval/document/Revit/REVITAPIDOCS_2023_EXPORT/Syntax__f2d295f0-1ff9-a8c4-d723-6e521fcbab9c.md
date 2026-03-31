[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method (XYZ, XYZ)

---



|  |
| --- |
| [BRepBuilderEdgeGeometry Class](b0051e1b-8b8b-f819-78c2-67053dd7a241.htm)   [See Also](#seeAlsoToggle) |

Constructs a BRepBuilderEdgeGeometry representing a straight line between the two given points.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public static BRepBuilderEdgeGeometry Create( 	XYZ startPoint, 	XYZ endPoint ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	startPoint As XYZ, _ 	endPoint As XYZ _ ) As BRepBuilderEdgeGeometry ``` |

 

| Visual C++ |
| --- |
| ``` public: static BRepBuilderEdgeGeometry^ Create( 	XYZ^ startPoint,  	XYZ^ endPoint ) ``` |

#### Parameters

startPoint
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)

endPoint
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentsInconsistentException](05972c68-fa6d-3a83-d720-ad84fbc4780f.htm) | The vectors startPoint and endPoint are coincident. |

# See Also

[BRepBuilderEdgeGeometry Class](b0051e1b-8b8b-f819-78c2-67053dd7a241.htm)

[Create Overload](aa204978-dafa-ac85-16ff-263981060a06.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)