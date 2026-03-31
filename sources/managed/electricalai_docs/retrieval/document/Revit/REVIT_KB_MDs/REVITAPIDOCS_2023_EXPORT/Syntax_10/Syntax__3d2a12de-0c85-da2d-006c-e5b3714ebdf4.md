[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetInsulationIds Method

---



|  |
| --- |
| [InsulationLiningBase Class](938d1b57-b9bb-44b0-81ec-c22dff57fc8e.htm)   [See Also](#seeAlsoToggle) |

Returns the ids of the insulation elements associated to a given element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static ICollection<ElementId> GetInsulationIds( 	Document document, 	ElementId elemId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetInsulationIds ( _ 	document As Document, _ 	elemId As ElementId _ ) As ICollection(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: static ICollection<ElementId^>^ GetInsulationIds( 	Document^ document,  	ElementId^ elemId ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

elemId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The element.

#### Return Value

A collection of the ids of the insulation elements.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | This id does not represent a valid host for insulation. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[InsulationLiningBase Class](938d1b57-b9bb-44b0-81ec-c22dff57fc8e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)