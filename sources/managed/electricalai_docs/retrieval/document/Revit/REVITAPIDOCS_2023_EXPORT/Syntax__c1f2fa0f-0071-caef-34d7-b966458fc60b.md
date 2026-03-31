[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DocumentId Property

---



|  |
| --- |
| [DocumentClosingEventArgs Class](939d187e-051c-6a8a-0bb9-6c030b0911a4.htm)   [See Also](#seeAlsoToggle) |

Id of the document that is about to be closed.

**Namespace:**   [Autodesk.Revit.DB.Events](b86712d6-83b3-e044-8016-f9881ecd3800.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2010

# Syntax

| C# |
| --- |
| ``` public int DocumentId { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property DocumentId As Integer 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property int DocumentId { 	int get (); } ``` |

# Remarks

This Id is only used to identify the document for the duration of this event and the DocumentClosed event which follows. It serves as synchronization means for the pair of events.

# See Also

[DocumentClosingEventArgs Class](939d187e-051c-6a8a-0bb9-6c030b0911a4.htm)

[Autodesk.Revit.DB.Events Namespace](b86712d6-83b3-e044-8016-f9881ecd3800.htm)