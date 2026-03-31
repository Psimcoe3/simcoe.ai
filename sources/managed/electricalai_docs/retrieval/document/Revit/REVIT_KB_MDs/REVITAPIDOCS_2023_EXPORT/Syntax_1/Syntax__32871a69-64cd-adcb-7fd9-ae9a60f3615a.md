[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetOrCreateWorksharingDisplaySettings Method

---



|  |
| --- |
| [WorksharingDisplaySettings Class](ec25e291-6582-7e8c-f273-efc0c391bcc4.htm)   [See Also](#seeAlsoToggle) |

Returns the worksharing display settings for the document, creating new settings for the current user if necessary.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static WorksharingDisplaySettings GetOrCreateWorksharingDisplaySettings( 	Document doc ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetOrCreateWorksharingDisplaySettings ( _ 	doc As Document _ ) As WorksharingDisplaySettings ``` |

 

| Visual C++ |
| --- |
| ``` public: static WorksharingDisplaySettings^ GetOrCreateWorksharingDisplaySettings( 	Document^ doc ) ``` |

#### Parameters

doc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document of interest.

#### Return Value

The worksharing display settings for the document.

# Remarks

Note that these settings are available even in models that are not workshared. This is to allow pre-configuring the display settings before enabling worksets so that they can be stored in template files.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | doc is not a project document. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[WorksharingDisplaySettings Class](ec25e291-6582-7e8c-f273-efc0c391bcc4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)