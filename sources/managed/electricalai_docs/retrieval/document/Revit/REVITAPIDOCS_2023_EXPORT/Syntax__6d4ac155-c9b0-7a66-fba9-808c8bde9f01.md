[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetEdgeReference Method

---



|  |
| --- |
| [PointOnEdgeFaceIntersection Class](3ade0249-e172-0bc2-32d6-9076f6b079cb.htm)   [See Also](#seeAlsoToggle) |

Change the edge or curve reference.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public void SetEdgeReference( 	Reference edgeReference ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetEdgeReference ( _ 	edgeReference As Reference _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetEdgeReference( 	Reference^ edgeReference ) ``` |

#### Parameters

edgeReference
:   Type:  [Autodesk.Revit.DB Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)

# Remarks

The referenced element may be any model element, including FamilyInstance, FormElement, or CurveElement. The reference must be of type ElementReferenceType.REFERENCE\_TYPE\_LINEAR.

# See Also

[PointOnEdgeFaceIntersection Class](3ade0249-e172-0bc2-32d6-9076f6b079cb.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)