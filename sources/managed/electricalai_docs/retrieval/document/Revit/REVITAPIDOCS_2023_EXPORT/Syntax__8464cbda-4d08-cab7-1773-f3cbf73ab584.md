[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsEqual Method

---



|  |
| --- |
| [DocumentVersion Class](3574fa56-016e-b146-1499-b3b1c9129705.htm)   [See Also](#seeAlsoToggle) |

Checks whether two DocumentVersions are identical. They are identical if both the GUID and number of saves are equal. If two DocumentVersions are identical, they come from the same document, with the same set of changes.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public bool IsEqual( 	DocumentVersion other ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsEqual ( _ 	other As DocumentVersion _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsEqual( 	DocumentVersion^ other ) ``` |

#### Parameters

other
:   Type:  [Autodesk.Revit.DB DocumentVersion](3574fa56-016e-b146-1499-b3b1c9129705.htm)    
     The DocumentVersion to compare to this DocumentVersion.

#### Return Value

True if the two DocumentVersions are equal. False otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[DocumentVersion Class](3574fa56-016e-b146-1499-b3b1c9129705.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)