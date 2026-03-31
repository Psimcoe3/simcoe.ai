[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsTranslation Property

---



|  |
| --- |
| [Transform Class](58dd01c8-b3fc-7142-e4f3-c524079a282d.htm)   [See Also](#seeAlsoToggle) |

The boolean value that indicates whether this transformation is a translation.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool IsTranslation { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property IsTranslation As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsTranslation { 	bool get (); } ``` |

# Remarks

This property is true if the only effect of transformation is translation. It checks that the basis of the transform is identity. The translation vector may be zero (which would make this an identity transformation) or nonzero (which would make this a non-trivial translation).

# See Also

[Transform Class](58dd01c8-b3fc-7142-e4f3-c524079a282d.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)