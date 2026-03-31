[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsExternalFileReference Method

---



|  |
| --- |
| [ExternalFileUtils Class](d6c4104f-ded9-29a4-2296-e1795b0da42a.htm)   [See Also](#seeAlsoToggle) |

Determines whether the given element represents an external file.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static bool IsExternalFileReference( 	Document aDoc, 	ElementId elemId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsExternalFileReference ( _ 	aDoc As Document, _ 	elemId As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsExternalFileReference( 	Document^ aDoc,  	ElementId^ elemId ) ``` |

#### Parameters

aDoc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     A Revit Document.

elemId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The element to be checked for an external file reference.

#### Return Value

True if the given element represents an external file; false otherwise.

# Remarks

CAD imports are not external file references, as their data is brought fully into Revit. No connection is maintained to the original file.

A link may be an external resource without being an external file.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The element elemId does not exist in the document |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ExternalFileUtils Class](d6c4104f-ded9-29a4-2296-e1795b0da42a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)