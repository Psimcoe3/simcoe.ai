[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ModifySubElement Method (SlabShapeVertex, Double)

---



|  |
| --- |
| [SlabShapeEditor Class](06308ccc-46e7-6ff8-582c-6891af8b75e9.htm)   [See Also](#seeAlsoToggle) |

Manipulates the vertex on the corresponding slab, roof or floor.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public void ModifySubElement( 	SlabShapeVertex vertex, 	double offset ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub ModifySubElement ( _ 	vertex As SlabShapeVertex, _ 	offset As Double _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void ModifySubElement( 	SlabShapeVertex^ vertex,  	double offset ) ``` |

#### Parameters

vertex
:   Type:  [Autodesk.Revit.DB SlabShapeVertex](8c022b91-723f-045d-3024-8cb037a41acc.htm)    
     The vertex.

offset
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The new value of the vertex offset.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the vertex is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when the vertex is invalid. |

# See Also

[SlabShapeEditor Class](06308ccc-46e7-6ff8-582c-6891af8b75e9.htm)

[ModifySubElement Overload](8f30639c-4eb0-1645-1fc3-26e0b6bfaa50.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)