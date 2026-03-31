[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StructuralUsage Property

---



|  |
| --- |
| [Wall Class](b5891733-c602-12df-beab-da414b58d608.htm)   [See Also](#seeAlsoToggle) |

Retrieves or changes the wall's designated structural usage.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public StructuralWallUsage StructuralUsage { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property StructuralUsage As StructuralWallUsage 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property StructuralWallUsage StructuralUsage { 	StructuralWallUsage get (); 	void set (StructuralWallUsage value); } ``` |

#### Field Value

The wall's designated structural usage, such as bearing or non bearing.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The enum value is not invalid for StructuralWallUsage. -or- When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[Wall Class](b5891733-c602-12df-beab-da414b58d608.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)