[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DeckProfileId Property

---



|  |
| --- |
| [CompoundStructureLayer Class](faece83a-6d49-41b0-2713-fe6cfaa5a3b5.htm)   [See Also](#seeAlsoToggle) |

The ElementId of the structural deck profile - only for a layer whose function is StructuralDeck.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public ElementId DeckProfileId { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property DeckProfileId As ElementId 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ DeckProfileId { 	ElementId^ get (); 	void set (ElementId^ value); } ``` |

#### Field Value

The default is InvalidElementId.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[CompoundStructureLayer Class](faece83a-6d49-41b0-2713-fe6cfaa5a3b5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)