[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DeleteWorkset Method

---



|  |
| --- |
| [WorksetTable Class](9ffa5fc8-e6a5-17d6-590e-8ecbfd7b85fb.htm)   [See Also](#seeAlsoToggle) |

Delete the specific workset.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2022.1

# Syntax

| C# |
| --- |
| ``` public static void DeleteWorkset( 	Document document, 	WorksetId worksetId, 	DeleteWorksetSettings deleteWorksetSettings ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Sub DeleteWorkset ( _ 	document As Document, _ 	worksetId As WorksetId, _ 	deleteWorksetSettings As DeleteWorksetSettings _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: static void DeleteWorkset( 	Document^ document,  	WorksetId^ worksetId,  	DeleteWorksetSettings^ deleteWorksetSettings ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document containing the worksets.

worksetId
:   Type:  [Autodesk.Revit.DB WorksetId](8bece327-c269-8101-b4c2-38632f593fe6.htm)    
     The id of the workset to delete.

deleteWorksetSettings
:   Type:  [Autodesk.Revit.DB DeleteWorksetSettings](1952e14e-42d8-d672-0e72-d5fb1a83b73a.htm)    
     The settings to delete a workset.

# Remarks

Please checkout the workset before executing this method. The method may fail in some situations that mentioned in  [CanDeleteWorkset(Document, WorksetId, DeleteWorksetSettings)](6a120bcb-6b51-f8c4-2f59-e21b15c31b6a.htm)  . Another failure case is the Transaction failure due to "Deleting all open views in a project is not allowed."

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | document is not a workshared document. -or- document is not a primary document, it is a linked document. -or- document is read-only: It cannot be modified. -or- There is no workset in the document with this id. -or- Workset cannot be deleted. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document has no open transaction. |
| [Autodesk.Revit.Exceptions RegenerationFailedException](787bb389-74c2-5ce7-cdd6-32211209ded2.htm) | The document regeneration fails during the DeleteWorkset operation. |

# See Also

[WorksetTable Class](9ffa5fc8-e6a5-17d6-590e-8ecbfd7b85fb.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)