[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FailuresAccessor Members

---



|  |
| --- |
| [FailuresAccessor Class](dea68b06-a061-fc05-d814-db741f2e7f14.htm)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [FailuresAccessor](dea68b06-a061-fc05-d814-db741f2e7f14.htm)  type exposes the following members.

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [CanCommitPendingTransaction](ad0c9f51-c915-08dc-c2a1-544055c74254.htm) | Checks if pending failure processing can be finished by committing a pending transaction. |
| Public method | [CanRollBackPendingTransaction](f84e1f4a-141c-8441-f920-cb697a555002.htm) | Checks if pending failure processing can be finished by rolling back a pending transaction. |
| Public method | [CommitPendingTransaction](e747579a-a5cc-623e-3091-c398ef4f1bc3.htm) | Finishes pending failures processing by committing the pending transaction. |
| Public method | [DeleteAllWarnings](c7f9d1a3-6fc0-7aaf-33da-3b31b3ab413e.htm) | Deletes all FailureMessages of severity "Warning" currently posted in a document. |
| Public method | [DeleteElements](bb23c934-3314-b5ef-7fbc-22cccd0aba84.htm) | Resolves failures by deletion of elements related to the failures. |
| Public method | [DeleteWarning](610d703e-eff2-690e-e04c-46edac21caa9.htm) | Deletes one specific failure message of severity "Warning". |
| Public method | [Dispose](8c30f9da-21a3-42ee-cd04-97f86b42bb71.htm) | Releases all resources used by the  [FailuresAccessor](dea68b06-a061-fc05-d814-db741f2e7f14.htm) |
| Public method | [Equals](http://msdn2.microsoft.com/en-us/library/bsc2ak47) | Determines whether the specified  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  is equal to the current  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  . (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetAttemptedResolutionTypes](442f5727-d827-033d-fd50-4daf1cf77d5d.htm) | Returns list of the failure resolution types attempted for the failure in the current transaction. |
| Public method | [GetDocument](f19901b5-9cba-bdbb-10a6-4ced16d2605f.htm) | Provides access to a document for which failures are being processed or preprocessed. |
| Public method | [GetFailureHandlingOptions](eff2181d-b026-4c4b-b14c-e9c62bbbc01c.htm) | Provides access to the failure handling options for the transaction currently being finished. |
| Public method | [GetFailureMessages](f8f03cd4-a151-91c6-4569-24597604cc81.htm) | Provides access to the individual failure messages currently posted in the document. |
| Public method | [GetFailureMessages(FailureSeverity)](1a24ee05-1057-4638-0b15-1a0f0ef0c21d.htm) | Provides access to the individual failure messages if a given severity currently posted in the document. |
| Public method | [GetHashCode](http://msdn2.microsoft.com/en-us/library/zdee4b3y) | Serves as a hash function for a particular type. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetSeverity](4ee2ef37-cc39-0464-d587-ed0bfdea4aa7.htm) | Provides access to the current failure severity. |
| Public method | [GetTransactionName](b7ace76a-4b1e-d175-e04c-b20bf57b38ea.htm) | Retrieves the name of the transaction for which failures are being processed. |
| Public method | [GetType](http://msdn2.microsoft.com/en-us/library/dfwy45w9) | Gets the  [Type](http://msdn2.microsoft.com/en-us/library/42892f65)  of the current instance. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [IsActive](ea3282f1-d68c-813e-394a-2d98bfae66dd.htm) | Method allows to check if this instance of the accessor is currently active. |
| Public method | [IsElementsDeletionPermitted](36a8ce51-3c76-8c7d-832d-4b250c585bf7.htm) | Checks if resolution of the failures by deleting failure elements is permitted. |
| Public method | [IsElementsDeletionPermitted(IList ElementId )](d6bc3b54-d1a5-ee5b-3c58-64370f1129ca.htm) | Checks if resolution of the failures by deleting given collection of elements is permitted. |
| Public method | [IsElementsDeletionPermitted(IList ElementId , String )](d138c9cb-b343-d38e-c4c9-a22ffd6baae4.htm) | Checks if resolution of the failures by deleting given collection of elements is permitted. |
| Public method | [IsFailureResolutionPermitted](4c6bd02b-cb12-a14d-0861-ce468c229d93.htm) | Checks if resolution of failures is permitted. |
| Public method | [IsFailureResolutionPermitted(FailureMessageAccessor)](50296b62-531f-c650-1c16-81d4a891603d.htm) | Checks if default resolution of the failure is permitted. |
| Public method | [IsFailureResolutionPermitted(FailureMessageAccessor, FailureResolutionType)](72c298ca-57c1-b008-3dcd-21f88eb47ab1.htm) | Checks if resolution of the failure using given resolution type is permitted. |
| Public method | [IsPending](7d67bf43-a961-de7f-fa6e-17d8eb4d2a63.htm) | Checks if the failure processing is pending. |
| Public method | [IsTransactionBeingCommitted](b8a411f9-da82-955f-11c2-85df810a6da2.htm) | Checks if the transaction for which failures are processed is being committed or rolled back. |
| Public method | [JournalFailures](a8638703-bf49-d2c5-fa4f-477ec919d854.htm) | Allows to record information about failures in the journal. |
| Public method | [PostFailure](5d25d459-a1b0-eef4-4766-b00bd1f5ba79.htm) | Posts an additional failure message to be processed for the current transaction. |
| Public method | [ReplaceFailures](b3377b4f-ea8b-4369-be9c-baaedf183b08.htm) | Deletes all failure messages currently posted in a document and replaces them with one "generic" failure. |
| Public method | [ResolveFailure](ee6c044d-28f4-9cec-c83c-883b604c8a7b.htm) | Resolves one failure using the failure resolution type last set for it. |
| Public method | [ResolveFailures](1a14a55b-ae8c-4cca-de65-51e2a1d24c9c.htm) | Resolves one or more failures using last set failure resolution type for each of the failures. If failure resolution type was not set for some of failures, default failure resolution type will be used. |
| Public method | [RollBackPendingTransaction](6f8caecd-0c82-658c-f209-eb91ea7fb5c6.htm) | Finishes pending failures processing by rolling back the pending transaction. |
| Public method | [SetFailureHandlingOptions](365c5204-4374-4ddc-6ccb-9d11d2926897.htm) | Sets failure handling options for the transaction currently being finished. |
| Public method | [SetTransactionName](89070a80-b41f-f42f-1746-28893aef91f7.htm) | Changes the name of the transaction for which failures are being processed. |
| Public method | [ToString](http://msdn2.microsoft.com/en-us/library/7bxwbwt2) | Returns a string that represents the current object. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [IsValidObject](f04d247c-f5a2-0589-8c53-abdd57d2897f.htm) | Specifies whether the .NET object represents a valid Revit entity. |

# See Also

[FailuresAccessor Class](dea68b06-a061-fc05-d814-db741f2e7f14.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)