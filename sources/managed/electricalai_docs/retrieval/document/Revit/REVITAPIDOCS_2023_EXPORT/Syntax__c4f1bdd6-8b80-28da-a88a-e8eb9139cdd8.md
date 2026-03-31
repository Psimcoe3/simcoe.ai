[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetRebarShapeId Method

---



|  |
| --- |
| [RebarShapeDrivenAccessor Class](6d2f77e7-bbe2-5bd5-723a-bf27c3df1a65.htm)   [See Also](#seeAlsoToggle) |

Changes the RebarShape element that defines the shape of the rebar. Changing the value of this member causes the Rebar instance to choose values for its shape parameters to preserve its previous shape as closely as possible

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public void SetRebarShapeId( 	ElementId shapeId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetRebarShapeId ( _ 	shapeId As ElementId _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetRebarShapeId( 	ElementId^ shapeId ) ``` |

#### Parameters

shapeId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | shapeId is not the id of a RebarShape in the document. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Structural. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This RebarShapeDrivenAccessor doesn't contain a valid rebar reference. |

# See Also

[RebarShapeDrivenAccessor Class](6d2f77e7-bbe2-5bd5-723a-bf27c3df1a65.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)