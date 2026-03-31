[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### VersionGuid Property

---



|  |
| --- |
| [Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)   [See Also](#seeAlsoToggle) |

Get the element version Guid.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public Guid VersionGuid { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property VersionGuid As Guid 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property Guid VersionGuid { 	Guid get (); } ``` |

# Remarks

If element version Guid is the same for a certain element in two instances of the saved file then we guarantee that the two elements are identical. One element version covers a period of time that is larger than a single transaction: it is a period between two saves, synchronize to central and reload latest. Thus, in an opened document in-between saves or synchronize actions, this version cannot be used to determine if any particular element has changed. To watch for element changes happening in-session, use event  [!:Autodesk::Revit::ApplicationServices::Application::DocumentChanged]  .

# See Also

[Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)