[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ProjectLocations Property

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [See Also](#seeAlsoToggle) |

Retrieve all the project locations associated with this project

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public ProjectLocationSet ProjectLocations { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property ProjectLocations As ProjectLocationSet 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property ProjectLocationSet^ ProjectLocations { 	ProjectLocationSet^ get (); } ``` |

# Remarks

This property returns all the locations of the project. A project can have one site location but many project locations within that site. Each project location object is an offset and rotation from the site location.

# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)