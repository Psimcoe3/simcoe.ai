[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetAllRevisionIds Method

---



|  |
| --- |
| [Revision Class](af882c60-68ae-2e53-5c41-7aa43cfc1df4.htm)   [See Also](#seeAlsoToggle) |

Returns the ids of all Revisions in the project ordered by sequence number.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public static IList<ElementId> GetAllRevisionIds( 	Document document ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetAllRevisionIds ( _ 	document As Document _ ) As IList(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: static IList<ElementId^>^ GetAllRevisionIds( 	Document^ document ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document containing the Revisions.

#### Return Value

The ids of all the Revisions in the document ordered by sequence number.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | document is not a project document. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[Revision Class](af882c60-68ae-2e53-5c41-7aa43cfc1df4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)