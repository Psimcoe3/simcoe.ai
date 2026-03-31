[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddBendVariableRadius Method

---



|  |
| --- |
| [RebarShapeDefinitionBySegments Class](7229fdba-1e8f-6cb7-e72e-0933e495ad62.htm)   [See Also](#seeAlsoToggle) |

Specify a variable-radius bend.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public void AddBendVariableRadius( 	int vertexIndex, 	RebarShapeVertexTurn turn, 	RebarShapeBendAngle angle, 	ElementId paramId, 	bool measureIncludingBarThickness ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub AddBendVariableRadius ( _ 	vertexIndex As Integer, _ 	turn As RebarShapeVertexTurn, _ 	angle As RebarShapeBendAngle, _ 	paramId As ElementId, _ 	measureIncludingBarThickness As Boolean _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void AddBendVariableRadius( 	int vertexIndex,  	RebarShapeVertexTurn turn,  	RebarShapeBendAngle angle,  	ElementId^ paramId,  	bool measureIncludingBarThickness ) ``` |

#### Parameters

vertexIndex
:   Type:  System Int32    
     Index of the vertex (1 to NumberOfVertices - 2).

turn
:   Type:  [Autodesk.Revit.DB.Structure RebarShapeVertexTurn](a59971ec-c31f-a05e-e2d7-65882e23a21f.htm)    
     Specify turn direction (RebarShapeVertexTurn::Left or RebarShapeVertexTurn::Right).

angle
:   Type:  [Autodesk.Revit.DB.Structure RebarShapeBendAngle](176a9649-853e-f173-c108-d6722fcd5b61.htm)    
     Specify whether the bend is acute, obtuse, etc.

paramId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Id of a parameter driving the radius.

measureIncludingBarThickness
:   Type:  System Boolean    
     If true, the radius is measured to the outside of the bend; if false, it is measured to the inside.

# Remarks

You must add a bend between each two segments.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | vertexIndex is not between 0 and NumberOfVertices. -or- paramId is not the id of a shared parameter in the current document, or its unit type is not UT\_Reinforcement\_Length or UT\_Angle. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[RebarShapeDefinitionBySegments Class](7229fdba-1e8f-6cb7-e72e-0933e495ad62.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)