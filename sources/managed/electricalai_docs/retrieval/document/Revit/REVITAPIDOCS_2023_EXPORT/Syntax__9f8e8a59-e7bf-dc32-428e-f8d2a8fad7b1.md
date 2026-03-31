[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ContainsKey Method

---



|  |
| --- |
| [ExportLayerTable Class](e68ce1c7-a922-d1b7-53bb-f832a4bad273.htm)   [See Also](#seeAlsoToggle) |

Checks whether a layer key exists in the table.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public bool ContainsKey( 	ExportLayerKey exportlayerKey ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function ContainsKey ( _ 	exportlayerKey As ExportLayerKey _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool ContainsKey( 	ExportLayerKey^ exportlayerKey ) ``` |

#### Parameters

exportlayerKey
:   Type:  [Autodesk.Revit.DB ExportLayerKey](64d77004-5c0c-9af2-cae4-39448bbaffe9.htm)    
     The export layer Key.

#### Return Value

True if the layer key exists in the table.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ExportLayerTable Class](e68ce1c7-a922-d1b7-53bb-f832a4bad273.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)