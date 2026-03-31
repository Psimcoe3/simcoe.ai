[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FindByName Method

---



|  |
| --- |
| [ExportDWGSettings Class](a17fc52f-f67a-9763-e52f-29f867106908.htm)   [See Also](#seeAlsoToggle) |

Returns the pre-defined non-in-session exporting settings for DWG in the given document with the specified name.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public static ExportDWGSettings FindByName( 	Document aDoc, 	string name ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function FindByName ( _ 	aDoc As Document, _ 	name As String _ ) As ExportDWGSettings ``` |

 

| Visual C++ |
| --- |
| ``` public: static ExportDWGSettings^ FindByName( 	Document^ aDoc,  	String^ name ) ``` |

#### Parameters

aDoc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     A Revit document to retrieve the specified pre-defined exporting settings for DWG.

name
:   Type:  System String    
     The name of the settings to retrieve.

#### Return Value

The pre-defined DWG exporting settings, or null if nothing found that has the corresponding name.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ExportDWGSettings Class](a17fc52f-f67a-9763-e52f-29f867106908.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)