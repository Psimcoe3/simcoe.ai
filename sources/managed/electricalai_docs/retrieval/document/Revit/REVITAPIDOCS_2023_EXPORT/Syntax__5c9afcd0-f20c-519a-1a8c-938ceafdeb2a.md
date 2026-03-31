[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HasAssociatedParts Method (Document, LinkElementId)

---



|  |
| --- |
| [PartUtils Class](a7384ccf-cd2b-9080-38d3-58b1253cd8e4.htm)   [See Also](#seeAlsoToggle) |

Checks if an element has associated parts.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static bool HasAssociatedParts( 	Document hostDocument, 	LinkElementId hostOrLinkElementId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function HasAssociatedParts ( _ 	hostDocument As Document, _ 	hostOrLinkElementId As LinkElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool HasAssociatedParts( 	Document^ hostDocument,  	LinkElementId^ hostOrLinkElementId ) ``` |

#### Parameters

hostDocument
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

hostOrLinkElementId
:   Type:  [Autodesk.Revit.DB LinkElementId](6e18abde-8787-9906-8576-ab0c9c5432c6.htm)    
     The element to be checked for associated Parts.

#### Return Value

True if the element has associated Parts.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[PartUtils Class](a7384ccf-cd2b-9080-38d3-58b1253cd8e4.htm)

[HasAssociatedParts Overload](55cd42e2-3eca-3592-336c-197c0c525c52.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)