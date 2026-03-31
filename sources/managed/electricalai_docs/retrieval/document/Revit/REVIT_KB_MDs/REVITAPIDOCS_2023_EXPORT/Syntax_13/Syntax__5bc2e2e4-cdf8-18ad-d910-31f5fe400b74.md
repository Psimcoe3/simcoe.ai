[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### UnpostFailure Method

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [See Also](#seeAlsoToggle) |

Deletes the posted failure message associated with a given FailureMessageKey.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public void UnpostFailure( 	FailureMessageKey messageKey ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub UnpostFailure ( _ 	messageKey As FailureMessageKey _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void UnpostFailure( 	FailureMessageKey^ messageKey ) ``` |

#### Parameters

messageKey
:   Type:  [Autodesk.Revit.DB FailureMessageKey](f0fa1b40-5df3-ddaf-e38d-85bd438a89e3.htm)    
     The key of the FailureMessage to be deleted.

# Remarks

If code that previously has posted a failure is executed again or otherwise detects that failure conditions do not exist anymore and the failure is not longer relevant, it should delete a failure message in order to let transaction to be committed. In order to delete the failure, it should invoke this method with a message key that was returned when the failure was posted.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | messageKey is invalid |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document has no open transaction. |

# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)