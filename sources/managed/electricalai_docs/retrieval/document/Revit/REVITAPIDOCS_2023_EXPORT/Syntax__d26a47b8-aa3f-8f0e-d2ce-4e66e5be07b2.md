[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Definitions Property

---



|  |
| --- |
| [DefinitionGroup Class](f3556557-3140-3296-6321-475b952f9022.htm)   [See Also](#seeAlsoToggle) |

The Definitions property returns an object that contains all the shared parameter definitions within the group.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public Definitions Definitions { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Definitions As Definitions 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property Definitions^ Definitions { 	Definitions^ get (); } ``` |

# Remarks

A known definition can be retrieved, by name, using the Item property on the Definitions object. A new definition can be created by using the Create method. The Create method takes two parameters, a string for name and a type. If the creation of the definition was successful then an object representing the definition is returned by the Create method.

# See Also

[DefinitionGroup Class](f3556557-3140-3296-6321-475b952f9022.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)