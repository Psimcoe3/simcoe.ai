[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsEqual Method

---



|  |
| --- |
| [CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.htm)   [See Also](#seeAlsoToggle) |

Checks whether this CompoundStructure is the same as another CompoundStructure.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public bool IsEqual( 	CompoundStructure otherStructure ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsEqual ( _ 	otherStructure As CompoundStructure _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsEqual( 	CompoundStructure^ otherStructure ) ``` |

#### Parameters

otherStructure
:   Type:  [Autodesk.Revit.DB CompoundStructure](dc1a081e-8dab-565f-145d-a429098d353c.htm)    
     A CompoundStructure.

#### Return Value

True if the two CompoundStructures are the same, and false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)