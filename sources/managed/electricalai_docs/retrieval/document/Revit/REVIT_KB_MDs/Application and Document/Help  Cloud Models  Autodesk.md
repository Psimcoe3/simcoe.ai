---
created: 2026-01-28T20:43:07 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Cloud Models | Autodesk

> ## Excerpt
> Autodesk provides two different BIM 360 web portals and regions with different URLs. You can save your Revit cloud models to either:

---
## Basic Info

-   Document.IsModelInCloud indicates if the current document is located in the cloud.
-   Document.GetCloudModelPath() returns the cloud model path.

Autodesk provides two different BIM 360 web portals and regions with different URLs. You can save your Revit cloud models to either:

-   Autodesk Docs US, at [insight.b360.autodesk.com](https://insight.b360.autodesk.com/)
-   Autodesk Docs EU, at [insight.b360.eu.autodesk.com](https://insight.b360.eu.autodesk.com/)

The property

-   ModelPath.Region

returns the region of the account and project which contains this model. `ModelPathUtils.CloudRegionUS` and `ModelPathUtils.CloudRegionEMEA` return the region names of different Autodesk cloud services. They can be used as the first argument of the ModelPathUtils.ConvertCloudGUIDsToCloudPath() method.

## Open

To open a cloud-hosted model with `Application.OpenDocumentFile` a `ModelPath` is needed. Such a ModelPath is returned by the method `ModelPathUtils.ConvertCloudGUIDsToCloudPath()` whose inputs are a region, ProjectGUID, and ModelGUID.

-   Document.CloudModelGUID returns the Model GUID if it is stored in the cloud.
-   ModelPath.GetProjectGUID() returns the Project GUID.
-   Document.GetWorksharingCentralModelPath() returns the model path of the central model.

### Getting the CloudPath for a Model

The region argument for ConvertCloudGUIDsToCloudPath is a string type and should be either "US" or "EMEA", depending on which BIM 360 or Autodesk Docs region account and project the model is stored in.

-   US - [insight.b360.autodesk.com](https://insight.b360.autodesk.com/) - ModelPathUtils.CloudRegionUS
-   EU - [insight.b360.eu.autodesk.com](https://insight.b360.eu.autodesk.com/) - ModelPathUtils.CloudRegionEMEA

Depending on where the cloud model is stored, provide the appropriate region argument "US" or "EMEA", respectively.

To get a valid CloudPath with the Revit API call `ModelPathUtils.ConvertCloudGUIDsToCloudPath()`. You will need to register a Forge application and use the Forge Data Management API to get the project Guid and model Guid as the other two arguments.

The [Forge DM API reference on GET hubs](https://forge.autodesk.com/en/docs/data/v2/reference/http/hubs-GET) shows how to list the hubs your Forge application can access. You can filter out the accounts of interest using the `data.attributes.name` field. You can also get the region information here.

The [Forge DM API reference on GET project folder contents](https://forge.autodesk.com/en/docs/data/v2/reference/http/projects-project_id-folders-folder_id-contents-GET) shows how to list the folder contents you plan to open. You can filter out the relevant cloud model using the `included.attributes.name` field; the project Guid and model Guid information is provided in the `included.attributes.extension.data` field.

With these three pieces of information - region, project guid, and model guid - you can obtain a valid cloud path with the ModelPathUtils.ConvertCloudGUIDsToCloudPath method and then open the model with the OpenDocument or OpenAndActivateDocument methods.

### Getting the Forge ID for a Model

These methods allow you to identify the Forge IDs for Cloud Models:

-   Document.GetHubId(): ForgeDM hub id where the model is located
-   Document.GetProjectId(): ForgeDM project id where the model is located
-   Document.GetCloudFolderId(bool forceRefresh): ForgeDM folder id where the model is located
-   Document.GetCloudModelUrn(): A ForgeDM Urn identifying the model They return strings which will be empty for a document which is not a cloud model.

### IOpenFromCloudCallback

An implementation of interface `IOpenFromCloudCallback` can be specified to control Revit's behavior when opening the cloud model. `IOpenFromCloudCallback.OnOpenConflict` method is called when a conflict happens during the model opening.

It receives a value of enum `OpenConflictScenario` that describes the conflict:

-   Rollback indicates that the Central model is restored to an earlier version.
-   Relinquished indicates that Ownership to model elements is relinquished.
-   OutOfDate indicates that the model is out of date
-   VersionArchived indicates that last central version merged into the local model to open has been archived in the central model. Editing is limited to elements and worksets the user owns until Reload Latest or Synchronize with Central is conducted after the model is opened.

And it returns a value of enum `OpenConflictResult` that describes the action Revit should take:

-   KeepLocalChanges - Keeps the local changes and open the model
-   DiscardLocalChangesAndOpenLatestVersion - Discard the local changes and open the latest version of the model
-   DetachFromCentral - Detach the local model from its central model, with worksets preserved
-   Cancel

`DefaultOpenFromCloudCallback` class is the default callback used by an overload of the Application.OpenDocumentFile method. `DiscardLocalChangesAndOpenLatestVersion` is returned for all kinds of conflicts.

## Save

-   Document.SaveAsCloudModel() saves the current model as a cloud model in BIM 360 and supports upload of local workshared file into BIM 360 Design as a Revit Cloud Worksharing central model.
-   Document.SaveCloudModel() saves the current cloud model.

To save a local Revit file to the cloud as a workshared or non-workshared cloud model, you need to get the BIM 360 or Autodesk Docs account id, project id, folder id, and a model name. There are two ways to retrieve this information:

1.  From the web browser
2.  Using the Forge DM API

### SaveAsCloudModel Information from the Web Browser

Open a web browser, navigate to your project home page, and copy the URL: ![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/acc_guids_1.png)

The account id and project id are both GUID strings.

They can be extracted from the URL like this: ![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/acc_guids_extract_1.png)

Navigate to your target Autodesk Docs folder in the web browser and copy the URL: ![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/acc_guids_3.png)

The folder id is embedded in this URL; in this example, it is "urn:adsk.wipprod:fs.folder:co.Foe4ZYNhTTKOhCqKApQkoQ": ![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/acc_guids_extract_3.png)

With this information, you can save a local file which is opened in Revit to Autodesk document management as a cloud model with a call like this:

```
public void SaveAsCloud(Document currentDocument)
{
  Guid account = new Guid("a8d3b76e-cf23-4dd7-a090-9e893efcf949");
  Guid project = new Guid("bf46f5e3-285e-496f-be03-b5b1f8b1e154");
  string folder_id = "urn:adsk.wipemea:fs.folder:co.Jo68ieLRRcKvQr4fI2Q8uQ";
  string model_name = "rac_advanced_sample_project.rvt";

  currentDocument.SaveAsCloudModel(
    account, // account id
    project, // project id
    folder_id, // folder id
    model_name // model name
  );
}
```

### SaveAsCloudModel Information with Forge DM API

With your Forge application, you can:

-   List hubs with the [GET hubs API](https://forge.autodesk.com/en/docs/data/v2/reference/http/hubs-GET) to retrieve the region and account ids.
-   List projects the [GET projects API](https://forge.autodesk.com/en/docs/data/v2/reference/http/hubs-hub_id-projects-GET) to get all the projects of the given hub and their project ids.
-   List the top folders with the [GET top folders API](https://forge.autodesk.com/en/docs/data/v2/reference/http/hubs-hub_id-projects-project_id-topFolders-GET) to get all accessible top folders (depending on permission) and you their valid folder ids, or continue to get the nested folders with the [list folder contents API](https://forge.autodesk.com/en/docs/data/v2/reference/http/projects-project_id-folders-folder_id-contents-GET) until the target folder and its folder id is found and can be stored for later use.

With this information, you can save a local file opened in Revit to Autodesk document management as a cloud model using the same Revit API call as above.
