[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Groups Property

---



|  |
| --- |
| [GroupType Class](5ce7e921-2a43-d7f1-8ef9-8a397dd27b75.htm)   [See Also](#seeAlsoToggle) |

Retrieve a set of all the groups that have this type.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public GroupSet Groups { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Groups As GroupSet 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property GroupSet^ Groups { 	GroupSet^ get (); } ``` |

#### Return Value

A set of group objects that all share this group type.

# Remarks

All groups returned by this property belong to this group type. A groups type can be changed by using the GroupType property on the group object, in which case it will no longer belong to this type but it will belong to the new type instead.

# See Also

[GroupType Class](5ce7e921-2a43-d7f1-8ef9-8a397dd27b75.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)