[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddConstraintArcLength Method

---



|  |
| --- |
| [RebarShapeDefinitionByArc Class](a92742a5-9781-3691-ec78-5b318fbf5ad3.htm)   [See Also](#seeAlsoToggle) |

Specify a parameter to drive the arc length of the shape.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2009

# Syntax

| C# |
| --- |
| ``` public void AddConstraintArcLength( 	ElementId paramId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub AddConstraintArcLength ( _ 	paramId As ElementId _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void AddConstraintArcLength( 	ElementId^ paramId ) ``` |

#### Parameters

paramId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Id of a parameter to drive the constraint. To obtain the id of a shared parameter, call RebarShape.GetElementIdForExternalDefinition().

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[RebarShapeDefinitionByArc Class](a92742a5-9781-3691-ec78-5b318fbf5ad3.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)