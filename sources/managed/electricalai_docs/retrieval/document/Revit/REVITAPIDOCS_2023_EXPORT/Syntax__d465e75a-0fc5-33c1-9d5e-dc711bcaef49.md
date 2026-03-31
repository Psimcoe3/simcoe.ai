[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsBackgroundCalculationInProgress Method

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [See Also](#seeAlsoToggle) |

Indicates whether there are any background calculations in progress for this document.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2019.1

# Syntax

| C# |
| --- |
| ``` public bool IsBackgroundCalculationInProgress() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsBackgroundCalculationInProgress As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsBackgroundCalculationInProgress() ``` |

#### Return Value

Returns true if the document has any data calculation in progress and false otherwise.

# Remarks

When a document has background calculations in progress, users cannot perform the following operations:

* Save/Close the document.
* Export/Print the document.
* Synchronize to central, in worksharing environment.
* Create a steel element.
* Copy/Mirror/Rotate a steel element.
* Edit the sketch of plate element.
* Edit a custom connection.

# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)