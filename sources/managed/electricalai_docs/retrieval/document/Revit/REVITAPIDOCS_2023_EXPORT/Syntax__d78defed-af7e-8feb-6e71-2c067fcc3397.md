[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetEndTreatmentTypeId Method

---



|  |
| --- |
| [RebarShape Class](0a370e32-eaba-785e-7e1f-9330929525fc.htm)   [See Also](#seeAlsoToggle) |

Gets the id of the EndTreatmentType at the specified rebar shape end.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public ElementId GetEndTreatmentTypeId( 	int iEnd ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetEndTreatmentTypeId ( _ 	iEnd As Integer _ ) As ElementId ``` |

 

| Visual C++ |
| --- |
| ``` public: ElementId^ GetEndTreatmentTypeId( 	int iEnd ) ``` |

#### Parameters

iEnd
:   Type:  System Int32    
     0 for the start end treatment, 1 for the end end treatment.

#### Return Value

Returns the id of an EndTreatmentType, or invalidElementId if the rebar shape has no end treatment at the specified end.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | iEnd not a valid shape end |

# See Also

[RebarShape Class](0a370e32-eaba-785e-7e1f-9330929525fc.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)