[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidDefaultTemplate Method

---



|  |
| --- |
| [ViewFamilyType Class](e0edeb6d-1627-3e3f-e386-be182a9dd8cb.htm)   [See Also](#seeAlsoToggle) |

Verifies that the input can be used as a default template for this view type.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public bool IsValidDefaultTemplate( 	ElementId templateId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsValidDefaultTemplate ( _ 	templateId As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsValidDefaultTemplate( 	ElementId^ templateId ) ``` |

#### Parameters

templateId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Id to be validated as default template.

#### Return Value

True if %templateId% is valid as default template, false otherwise.

# Remarks

The id must represent a template view that is compatible with this view type, or InvalidElementId.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ViewFamilyType Class](e0edeb6d-1627-3e3f-e386-be182a9dd8cb.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)