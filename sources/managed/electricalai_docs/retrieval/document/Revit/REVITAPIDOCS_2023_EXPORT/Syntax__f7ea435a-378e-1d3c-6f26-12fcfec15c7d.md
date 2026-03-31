[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetStructuralElementDefinitionData Method

---



|  |
| --- |
| [StructuralSectionUtils Class](4515469b-b4e9-43f6-13ee-293a91943a5d.htm)   [See Also](#seeAlsoToggle) |

Return structural element definition data.

**Namespace:**   [Autodesk.Revit.DB.Structure.StructuralSections](09862f38-63f6-a5f8-e560-ae775901bc92.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public static StructuralSectionErrorCode GetStructuralElementDefinitionData( 	Document document, 	ElementId elementId, 	out StructuralElementDefinitionData data ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetStructuralElementDefinitionData ( _ 	document As Document, _ 	elementId As ElementId, _ 	<OutAttribute> ByRef data As StructuralElementDefinitionData _ ) As StructuralSectionErrorCode ``` |

 

| Visual C++ |
| --- |
| ``` public: static StructuralSectionErrorCode GetStructuralElementDefinitionData( 	Document^ document,  	ElementId^ elementId,  	[OutAttribute] StructuralElementDefinitionData^% data ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document that owns the beam, brace or structural column.

elementId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     ID of family instance for beam, brace or structural column.

data
:   Type:  [Autodesk.Revit.DB.Structure.StructuralSections StructuralElementDefinitionData](f7a0e8ec-6fd5-43e5-1a54-5cb6ebe009c7.htm)   %    
     Structural element definition data.

#### Return Value

Success code is returned if StructuralElementDefinitionData was provided successfully, error code otherwise.

# Remarks

This information is provided only for beams, braces and structural columns.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[StructuralSectionUtils Class](4515469b-b4e9-43f6-13ee-293a91943a5d.htm)

[Autodesk.Revit.DB.Structure.StructuralSections Namespace](09862f38-63f6-a5f8-e560-ae775901bc92.htm)