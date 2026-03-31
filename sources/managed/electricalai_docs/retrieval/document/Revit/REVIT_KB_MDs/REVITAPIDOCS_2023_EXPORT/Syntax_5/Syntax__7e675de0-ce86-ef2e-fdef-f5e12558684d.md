[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsNotLoadedIntoMultipleOpenDocuments Method

---



|  |
| --- |
| [RevitLinkType Class](2204a5ab-6476-df41-116d-23dbe3cb5407.htm)   [See Also](#seeAlsoToggle) |

Checks whether the link is loaded into more than one open document in this session of Revit. If the link is loaded into multiple open documents, reload will be disabled.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public bool IsNotLoadedIntoMultipleOpenDocuments() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsNotLoadedIntoMultipleOpenDocuments As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsNotLoadedIntoMultipleOpenDocuments() ``` |

#### Return Value

True if the link is loaded into at most one open document. False if the link is loaded into more than one open document.

# Remarks

Revit can open several documents which contain the same link. If this is the case, Revit cannot reload the link, as doing so would make changes to a non-active document. You will need to close one or more documents in order to modify the link.

If the link is loaded into multiple documents across multiple sessions of Revit, this function will return true. We only check the current session of Revit. It is safe to reload a link which is loaded into multiple sessions, as long as it is not loaded into more than one document in any one session.

If this function returns true, it is safe to reload the link.

# See Also

[RevitLinkType Class](2204a5ab-6476-df41-116d-23dbe3cb5407.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)