[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidRebarShapeId Method

---



|  |
| --- |
| [PathReinforcement Class](1593a849-b883-73d4-7c02-a2522877d71d.htm)   [See Also](#seeAlsoToggle) |

Identifies whether an element id corresponds to a Rebar Shape element which can be used in Path Reinforcement.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static bool IsValidRebarShapeId( 	Document aDoc, 	ElementId elementId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsValidRebarShapeId ( _ 	aDoc As Document, _ 	elementId As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsValidRebarShapeId( 	Document^ aDoc,  	ElementId^ elementId ) ``` |

#### Parameters

aDoc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

elementId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     An element id.

#### Return Value

True if the specified element id corresponds to a Rebar Shape element.

# Remarks

The Rebar Shape has to be two dimensional shape only and its neighbouring segments may form only right angles.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[PathReinforcement Class](1593a849-b883-73d4-7c02-a2522877d71d.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)