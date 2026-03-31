[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TextNoteOptions Constructor (ElementId)

---



|  |
| --- |
| [TextNoteOptions Class](b0fd6ef8-a0ef-9cf4-5bc2-8cd65f81f648.htm)   [See Also](#seeAlsoToggle) |

Constructs text options to create text of the given type.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public TextNoteOptions( 	ElementId typeId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	typeId As ElementId _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: TextNoteOptions( 	ElementId^ typeId ) ``` |

#### Parameters

typeId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Id of a text type that defines the style of a text note.

# Remarks

Except for the TypeId, all other properties of the option class will be populated with their respective default values.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[TextNoteOptions Class](b0fd6ef8-a0ef-9cf4-5bc2-8cd65f81f648.htm)

[TextNoteOptions Overload](af52a85a-8736-4a77-f3e5-b9624a5bd2bf.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)