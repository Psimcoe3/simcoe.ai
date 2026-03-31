[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### EnableWorksharing Method

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [See Also](#seeAlsoToggle) |

Enables worksharing in the document.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public void EnableWorksharing( 	string worksetNameGridLevel, 	string worksetName ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub EnableWorksharing ( _ 	worksetNameGridLevel As String, _ 	worksetName As String _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void EnableWorksharing( 	String^ worksetNameGridLevel,  	String^ worksetName ) ``` |

#### Parameters

worksetNameGridLevel
:   Type:  System String    
     Name of workset for grids and levels.

worksetName
:   Type:  System String    
     Name of workset for all other elements.

# Remarks

The document's Undo history will be cleared by this command. As a result, this command and others executed before it cannot be undone.

All transaction phases (e.g. transactions transaction groups and sub-transaction) that were explicitly started must be finished prior to calling this method.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | worksetNameGridLevel is an empty string. -or- worksetName is an empty string. -or- worksetNameGridLevel cannot include prohibited characters, such as "{, }, [, ], |, ;, less-than sign, greater-than sign, ?, `, ~". -or- worksetName cannot include prohibited characters, such as "{, }, [, ], |, ;, less-than sign, greater-than sign, ?, `, ~". |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ForbiddenForDynamicUpdateException](c5b911f6-1e8f-2cd4-6965-286f41221fe0.htm) | This method may not be called during dynamic update. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The document does not allow worksharing to be enabled. -or- This Document is in an edit mode. -or- This Document is a workshared document. -or- There is a transaction phase left open (such as a transaction, sub-transaction of transaction group) at the time of invoking this method. |
| [Autodesk.Revit.Exceptions OperationCanceledException](aea34480-ceb5-b49f-129d-0799e7bb1c21.htm) | Enabling worksharing was cancelled. |

# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)