[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetRegisteredUpdaterInfos Method (Document)

---



|  |
| --- |
| [UpdaterRegistry Class](4f24f516-5274-1420-f255-458c0af5d318.htm)   [See Also](#seeAlsoToggle) |

Returns information about all updaters applicable to the given document.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public static IList<UpdaterInfo> GetRegisteredUpdaterInfos( 	Document document ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetRegisteredUpdaterInfos ( _ 	document As Document _ ) As IList(Of UpdaterInfo) ``` |

 

| Visual C++ |
| --- |
| ``` public: static IList<UpdaterInfo^>^ GetRegisteredUpdaterInfos( 	Document^ document ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document to which sought updaters are applicable to.

#### Return Value

List of UpdaterInfo structures

# Remarks

The list of data includes information about all updaters explicitly registered for the document as well as information about all application-wide registered updaters (which are applicable to all documents).

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[UpdaterRegistry Class](4f24f516-5274-1420-f255-458c0af5d318.htm)

[GetRegisteredUpdaterInfos Overload](541dfdf1-29ff-c7ec-b9b2-9d10426bf845.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)