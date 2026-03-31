[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ActiveProjectLocation Property

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [See Also](#seeAlsoToggle) |

Retrieve the active project location.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public ProjectLocation ActiveProjectLocation { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property ActiveProjectLocation As ProjectLocation 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ProjectLocation^ ActiveProjectLocation { 	ProjectLocation^ get (); 	void set (ProjectLocation^ value); } ``` |

# Remarks

Getting this property returns the currently active project location that the user is currently working with. Setting this property can be used to change the active project location.

# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)