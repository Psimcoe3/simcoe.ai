[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LoadItemFiles Method

---



|  |
| --- |
| [FabricationConfiguration Class](f7094105-2acf-03f1-7a7f-82dd24087a17.htm)   [See Also](#seeAlsoToggle) |

Loads the specified fabrication item files into the project.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2019

# Syntax

| C# |
| --- |
| ``` public IList<FabricationItemFile> LoadItemFiles( 	IList<FabricationItemFile> itemFiles ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function LoadItemFiles ( _ 	itemFiles As IList(Of FabricationItemFile) _ ) As IList(Of FabricationItemFile) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<FabricationItemFile^>^ LoadItemFiles( 	IList<FabricationItemFile^>^ itemFiles ) ``` |

#### Parameters

itemFiles
:   Type:  System.Collections.Generic IList   [FabricationItemFile](ccf31061-ac40-f869-0b9e-834a9c146427.htm)    
     The relative paths of the fabrication item files to load.

#### Return Value

The relative paths of the fabrication item files which failed to load.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The current fabrication configuration is not connected and updated to source configuration. Reload and try again. -or- this operation failed. |

# See Also

[FabricationConfiguration Class](f7094105-2acf-03f1-7a7f-82dd24087a17.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)