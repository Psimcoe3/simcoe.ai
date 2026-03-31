[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BuiltInFailures.LinkFailures Members

---



|  |
| --- |
| [BuiltInFailures LinkFailures Class](99f8c34f-60bc-2dc8-eb93-c8db7d276e53.htm)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

Provides a container of all Revit built-in FailureDefinitionId instances.

The  [BuiltInFailures LinkFailures](99f8c34f-60bc-2dc8-eb93-c8db7d276e53.htm)  type exposes the following members.

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property Static member | [CannotModifyLinkedFile](4637d266-f732-a072-a795-d3a71cd304e9.htm) | Shared Sites in the link ""%1!s!"" cannot be modified. |
| Public property Static member | [CannotOpenLinkedFileServerFound](428719cc-c399-8090-817a-900262bb3f16.htm) | Cannot open the linked model using Open and Unload because the plugin [name] provided by [vendor] experienced an error. For more information please contact [vendor]. |
| Public property Static member | [CannotOpenLinkedFileServerNotFound](85101fe8-8e47-b1a3-3f4b-5af667618041.htm) | Cannot open the linked model using Open and Unload because the plugin [name] cannot be accessed. Please check plugin [name], which has server Id [serverId] |
| Public property Static member | [CannotPublishSharedCoordinatesToMirroredNonRevitLinks](7fe8291b-b467-ed4c-b4a8-2f767377fd0a.htm) | Shared coordinates cannot be published to mirrored, non Revit, links. |
| Public property Static member | [CannotReloadFile](636e2b5e-be72-cc67-13da-6930df89e11e.htm) | Can't reload file. |
| Public property Static member | [CannotUnlinkFile](7fef6fe0-1536-68e0-76c8-f3a4ed783e85.htm) | Can't unlink file. |
| Public property Static member | [DataDictionaryDifferentInLink](3f6c39b5-2ca1-75be-6b03-0ab8d1a56e2e.htm) | Linked file [Name] was last saved in a previous version of Revit. Changes to it cannot be saved until it is upgraded. |
| Public property Static member | [DeleteLinkSymbolPrompt](a1186970-5a26-4ff8-1b9f-ee5f66e1cb19.htm) | All instances of Linked Model '[Name]' have been deleted, but the file itself is still loaded. Remove the Linked File using Manage Links dialog to save memory unless you are going to reuse it in this project. Removing the Link cannot be undone. |
| Public property Static member | [LinkedFileOpenInOtherDoc](e7c1e7b6-2cd9-35b4-f756-9210c16bcd46.htm) | Linked file cannot be reloaded because it is loaded into another open document. |
| Public property Static member | [LinkInstanceNeedsReconcile](82307566-0cbc-d760-0d6d-dc20c0442637.htm) | Instance of linked .rvt file needs Coordination Review |
| Public property Static member | [ModifiedLinkedFile](dfca3e75-7a24-1b88-1ceb-fa8bdc7b4592.htm) | Shared Sites in the link have been modified, use move instance to reset the change. |
| Public property Static member | [ModifyingLinkedFile](b01b729f-a4bd-0612-2080-b4559052cf53.htm) | Shared Locations in the Linked Model '[Name]' have been modified, but not saved back to the Linked File. Upon reopening, instances of the Linked Model will return to their last Saved Positions. You can Save the Linked Model later via the Manage Links dialog. |
| Public property Static member | [MultipleLinks](97754a6c-292f-ae9f-bc33-7683ba130e01.htm) | Can't complete operation. Linked Files have the same name. |
| Public property Static member | [NoConstraintsToLinks1](403697fb-4de4-fc72-df1c-8077f7281a38.htm) | Constraints may not be created to linked instances using Shared Locations. Constraints will be removed. |
| Public property Static member | [SourceFileDrivenByOtherTarget](f426e161-8942-738c-f012-03da68cda6b9.htm) | Linked Model's Shared Coordinates have been modified via another host model in this session. In order to be able to change the Linked File via the active host model, Save and open it again in a new session. |
| Public property Static member | [WatchedLinkMoved](7001c92a-9ddf-9422-777a-b507763b2ce2.htm) | Monitored Link moved. |

# See Also

[BuiltInFailures LinkFailures Class](99f8c34f-60bc-2dc8-eb93-c8db7d276e53.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)