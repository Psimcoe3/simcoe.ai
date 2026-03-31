[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Export Method (String, String, IFCExportOptions)

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [See Also](#seeAlsoToggle) |

Exports the document to the Industry Standard Classes (IFC) format.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public bool Export( 	string folder, 	string name, 	IFCExportOptions options ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function Export ( _ 	folder As String, _ 	name As String, _ 	options As IFCExportOptions _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool Export( 	String^ folder,  	String^ name,  	IFCExportOptions^ options ) ``` |

#### Parameters

folder
:   Type:  System String    
     Output folder into which the file will be exported. The folder must exist.

name
:   Type:  System String    
     Either the name of a single file or a prefix for a set of files. If empty, automatic naming will be used.

options
:   Type:  [Autodesk.Revit.DB IFCExportOptions](db8ed2bb-8949-7a7f-e09a-29f6c9916f42.htm)    
     Various options applicable to the IFC format. If    a null reference (  Nothing  in Visual Basic)  , all options will be set to their respective default values.

#### Return Value

True if successful, otherwise False.

# Remarks

Exporting to IFC requires that document is modifiable, therefore there must be a transaction already open when this method is called.

This method may not be invoked during dynamic update, for the internal routine might need to modify the existing transaction.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | NullOrEmpty -or- Contains invalid characters. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions FileArgumentNotFoundException](ca9ccaa9-ed08-d40d-31a7-1af3ad2dcb84.htm) | The IFCExportOptions FamilyMappingFile does not exist. |
| [Autodesk.Revit.Exceptions ForbiddenForDynamicUpdateException](c5b911f6-1e8f-2cd4-6965-286f41221fe0.htm) | This method may not be called during dynamic update. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Export is temporarily disabled. -or- Exporting is not allowed in the current application mode. -or- This Document is not a project document. |
| [Autodesk.Revit.Exceptions InvalidPathArgumentException](3f3c93a6-008b-f9de-40d4-5cd99bb32b34.htm) | The folder does not exist. |
| [Autodesk.Revit.Exceptions ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document has no open transaction. |
| [Autodesk.Revit.Exceptions OptionalFunctionalityNotAvailableException](0612a676-b6ba-8c37-2e28-b197438305ab.htm) | The IFC module is not available in the installed Revit. |

# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[Export Overload](2f535342-ee41-86f9-0022-92ba1f65112d.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)