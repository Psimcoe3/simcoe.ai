[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NewSlabEdge Method (SlabEdgeType, Reference)

---



|  |
| --- |
| [Document Class](ab1718f9-45fb-b3d3-827e-32ff81cf929c.htm)   [See Also](#seeAlsoToggle) |

Creates a slab edge along a reference.

**Namespace:**   [Autodesk.Revit.Creation](ded320da-058a-4edd-0418-0582389559a7.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)

# Syntax

| C# |
| --- |
| ``` public SlabEdge NewSlabEdge( 	SlabEdgeType SlabEdgeType, 	Reference reference ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function NewSlabEdge ( _ 	SlabEdgeType As SlabEdgeType, _ 	reference As Reference _ ) As SlabEdge ``` |

 

| Visual C++ |
| --- |
| ``` public: SlabEdge^ NewSlabEdge( 	SlabEdgeType^ SlabEdgeType,  	Reference^ reference ) ``` |

#### Parameters

SlabEdgeType
:   Type:  [Autodesk.Revit.DB SlabEdgeType](0f6f73b4-26b9-044e-590c-ef65a1210db8.htm)    
     The type of the slab edge to create

reference
:   Type:  [Autodesk.Revit.DB Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)    
     A planar line or arc that represents the place where you want to place the slab edge.

#### Return Value

If successful a new slab edge object within the project, otherwise    a null reference (  Nothing  in Visual Basic)  .

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown if the slab edge type does not exist in the given document. |

# See Also

[Document Class](ab1718f9-45fb-b3d3-827e-32ff81cf929c.htm)

[NewSlabEdge Overload](d9f19a39-e6db-01ef-ae8c-b491ca8cbc51.htm)

[Autodesk.Revit.Creation Namespace](ded320da-058a-4edd-0418-0582389559a7.htm)