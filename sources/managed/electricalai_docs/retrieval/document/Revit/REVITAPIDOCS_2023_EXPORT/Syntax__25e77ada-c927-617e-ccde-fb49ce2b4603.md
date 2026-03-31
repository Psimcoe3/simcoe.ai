[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ElementLevelFilter Constructor (ElementId, Boolean)

---



|  |
| --- |
| [ElementLevelFilter Class](844e4928-e11a-563f-b1e4-d4d16b8bd76b.htm)   [See Also](#seeAlsoToggle) |

Constructs a new instance of an ElementLevelFilter, with the option to match all elements not associated to the given level id.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public ElementLevelFilter( 	ElementId levelId, 	bool inverted ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	levelId As ElementId, _ 	inverted As Boolean _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: ElementLevelFilter( 	ElementId^ levelId,  	bool inverted ) ``` |

#### Parameters

levelId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of the level that will be matched to elements' associated level.

inverted
:   Type:  System Boolean    
     True if the filter should match all elements not associated to the given level.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ElementLevelFilter Class](844e4928-e11a-563f-b1e4-d4d16b8bd76b.htm)

[ElementLevelFilter Overload](d31291df-1c4e-df8b-7844-694f74682dad.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)