[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetExternalFileReference Method

---



|  |
| --- |
| [ExternalFileUtils Class](d6c4104f-ded9-29a4-2296-e1795b0da42a.htm)   [See Also](#seeAlsoToggle) |

Gets the external file referencing data for the given element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static ExternalFileReference GetExternalFileReference( 	Document aDoc, 	ElementId elemId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetExternalFileReference ( _ 	aDoc As Document, _ 	elemId As ElementId _ ) As ExternalFileReference ``` |

 

| Visual C++ |
| --- |
| ``` public: static ExternalFileReference^ GetExternalFileReference( 	Document^ aDoc,  	ElementId^ elemId ) ``` |

#### Parameters

aDoc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     A Revit Document.

elemId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The element whose external file reference we want.

#### Return Value

An object containing path and type information for the given element's external file.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The element elemId does not exist in the document -or- elemId does not represent an external file reference. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ExternalFileUtils Class](d6c4104f-ded9-29a4-2296-e1795b0da42a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)