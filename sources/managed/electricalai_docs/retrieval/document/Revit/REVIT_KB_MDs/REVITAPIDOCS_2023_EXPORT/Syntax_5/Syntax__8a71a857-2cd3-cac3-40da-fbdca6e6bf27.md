[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Add Method

---



|  |
| --- |
| [ExportPatternTable Class](3e87bc0e-e04b-f76a-2b06-82e951b5aec2.htm)   [See Also](#seeAlsoToggle) |

Inserts a (key,info) pair into Export pattern table.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public void Add( 	ExportPatternKey exportPatternKey, 	ExportPatternInfo exportPatternInfo ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub Add ( _ 	exportPatternKey As ExportPatternKey, _ 	exportPatternInfo As ExportPatternInfo _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void Add( 	ExportPatternKey^ exportPatternKey,  	ExportPatternInfo^ exportPatternInfo ) ``` |

#### Parameters

exportPatternKey
:   Type:  [Autodesk.Revit.DB ExportPatternKey](8e55a491-0886-37f5-b867-e4eea95276eb.htm)    
     The export pattern key to be added.

exportPatternInfo
:   Type:  [Autodesk.Revit.DB ExportPatternInfo](17621c1b-5f57-2a25-6ff9-73dfc67d5024.htm)    
     The export pattern info to be added.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The key already exists in the table. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ExportPatternTable Class](3e87bc0e-e04b-f76a-2b06-82e951b5aec2.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)