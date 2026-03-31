[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidForCreateParts Method

---



|  |
| --- |
| [PartUtils Class](a7384ccf-cd2b-9080-38d3-58b1253cd8e4.htm)   [See Also](#seeAlsoToggle) |

Identifies if the given element can be used to create parts.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static bool IsValidForCreateParts( 	Document document, 	LinkElementId hostOrLinkElementId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsValidForCreateParts ( _ 	document As Document, _ 	hostOrLinkElementId As LinkElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsValidForCreateParts( 	Document^ document,  	LinkElementId^ hostOrLinkElementId ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

hostOrLinkElementId
:   Type:  [Autodesk.Revit.DB LinkElementId](6e18abde-8787-9906-8576-ab0c9c5432c6.htm)    
     Id to be tested for validity for creating part.

#### Return Value

True if this id is valid, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[PartUtils Class](a7384ccf-cd2b-9080-38d3-58b1253cd8e4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)