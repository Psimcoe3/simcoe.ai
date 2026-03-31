[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SaveAsCloudModel Method (Guid, Guid, String, String)

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [See Also](#seeAlsoToggle) |

Saves current non-workshared or workshared model as a cloud model or workshared cloud model in BIM 360 Docs or Autodesk Docs.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public void SaveAsCloudModel( 	Guid accountId, 	Guid projectId, 	string folderId, 	string modelName ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SaveAsCloudModel ( _ 	accountId As Guid, _ 	projectId As Guid, _ 	folderId As String, _ 	modelName As String _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SaveAsCloudModel( 	Guid accountId,  	Guid projectId,  	String^ folderId,  	String^ modelName ) ``` |

#### Parameters

accountId
:   Type:  System Guid    
     The BIM 360 Docs or Autodesk Docs account Id. You can use one of the following methods to get this Id:

    * If you get the hub Id with Forge Data Management API, remove the prefix "b." of the Id string and convert the rest to a Guid.
    * If you get the account Id with Forge BIM 360 Docs or Autodesk Docs API, just convert the Id string to a Guid.

projectId
:   Type:  System Guid    
     The BIM 360 Docs or Autodesk Docs project Id. You can use one of the following methods to get this Id:

    * If you get the project Id with Forge Data Management API, remove the prefix "b." of the Id string and convert the rest to a Guid.
    * If you get the project Id with Forge BIM 360 Docs or Autodesk Docs API, just convert the Id string to a Guid.

folderId
:   Type:  System String    
     Folder identity in BIM 360 Docs or Autodesk Docs to save the model. You can use one of the following methods to get this Id:

    * The folder Id string from Forge Data Management API.
    * The folder Id string from Forge BIM 360 Docs or Autodesk Docs API.

modelName
:   Type:  System String    
     Model name in BIM 360 Docs or Autodesk Docs to save the model.

# Remarks

Assumes that user is currently signed in BIM 360 Docs or Autodesk Docs and has access to Autodesk cloud services. This operation will create a model on cloud and then create a local cache of the cloud model. This method cannot be used when current document is already in cloud.

You can use one of the following methods to save a local model as a workshared cloud model in BIM 360 Docs or Autodesk Docs.

* If the local model is a workshared model, then it will be a workshared cloud model after you use this method successfully.
* If the local model is a non-workshared model, you can enable the workset with  [EnableWorksharing(String, String)](7c29717e-1d8c-4e02-20ad-65c53ea8eaaa.htm)  and then save as a workshared cloud model.
* If the local model is a non-workshared model, and you have already saved it as a non-workshared cloud model in BIM 360 Docs or Autodesk Docs, you can still enable the workset with  [EnableCloudWorksharing](4146e816-565e-85d8-ce94-93ec505a0924.htm)  to convert it to a workshared cloud model.

You cannot save a local workshared model as a non-workshared cloud model in BIM 360 Docs or Autodesk Docs.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | folderId is an empty string. -or- modelName is an empty string. -or- The input file name "modelName" does not represent a valid file name. -or- Thrown when the input BIM 360 Docs or Autodesk Docs account Id or project Id is invalid or unmatched. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ForbiddenForDynamicUpdateException](c5b911f6-1e8f-2cd4-6965-286f41221fe0.htm) | SaveAs may not be called during dynamic update. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Saving is not allowed in the current application mode. -or- This Document is not a project document. -or- This Document is in an edit mode. -or- This Document is not a primary document, it is a linked document. -or- SaveAs is temporarily disabled. -or- This Document is a cloud model, cannot be saved as a cloud model. -or- There is a transaction phase left open (such as a transaction, sub-transaction of transaction group) at the time of invoking this method. |
| [Autodesk.Revit.Exceptions RevitServerCommunicationException](a0003d89-0113-6623-65da-0db5c568bfb6.htm) | Could be for any of the reasons related to network. |
| [Autodesk.Revit.Exceptions RevitServerInternalException](6dcd093c-d643-07cd-535f-36ffa9d2db52.htm) | Could be for any of the reasons that saveAs fails with RevitServerInternalException. |
| [Autodesk.Revit.Exceptions RevitServerModelAlreadyExistsException](a3ed0157-0a46-0b62-62db-08112e1645bd.htm) | Failed due to there is a model with the same name already exists at the specified location. |
| [Autodesk.Revit.Exceptions RevitServerModelNameBreaksConventionException](ec0e702a-f076-1b44-4277-feefd39045d4.htm) | Failed due to the model name is breaking project naming convention. |
| [Autodesk.Revit.Exceptions RevitServerUnauthenticatedUserException](b9b68e56-c767-4680-a65b-73d268ee8860.htm) | User is not signed in with Autodesk id. |
| [Autodesk.Revit.Exceptions RevitServerUnauthorizedException](9e8c1efc-8719-fe01-f311-cfade7b177ed.htm) | You don't have the entitlement to perform the operation to this this Document. -or- User is not authorized to access the specified cloud project. |

# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)