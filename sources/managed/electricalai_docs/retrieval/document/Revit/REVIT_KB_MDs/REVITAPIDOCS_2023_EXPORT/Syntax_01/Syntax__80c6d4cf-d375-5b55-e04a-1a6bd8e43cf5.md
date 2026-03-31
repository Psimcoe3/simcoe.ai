[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetValidFamiliesForNoteBlock Method

---



|  |
| --- |
| [ViewSchedule Class](0dae24ba-5dcb-9a34-cccc-0cf8cc52bcd3.htm)   [See Also](#seeAlsoToggle) |

Gets a list of families that can be used for a note block.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static ICollection<ElementId> GetValidFamiliesForNoteBlock( 	Document document ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetValidFamiliesForNoteBlock ( _ 	document As Document _ ) As ICollection(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: static ICollection<ElementId^>^ GetValidFamiliesForNoteBlock( 	Document^ document ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

#### Return Value

The IDs of all valid families.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ViewSchedule Class](0dae24ba-5dcb-9a34-cccc-0cf8cc52bcd3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)