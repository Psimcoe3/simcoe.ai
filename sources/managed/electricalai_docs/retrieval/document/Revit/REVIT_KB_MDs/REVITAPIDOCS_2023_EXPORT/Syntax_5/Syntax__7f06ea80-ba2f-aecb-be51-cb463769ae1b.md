[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsVerticallyHomogeneous Method

---



|  |
| --- |
| [CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.htm)   [See Also](#seeAlsoToggle) |

Indicates whether this CompoundStructure represents a single set of parallel layers.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool IsVerticallyHomogeneous() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsVerticallyHomogeneous As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsVerticallyHomogeneous() ``` |

#### Return Value

True if this CompoundStructure represents a series of parallel layers that stretch from bottom to top, false otherwise.

# Remarks

Differs from IsVerticallyCompound as a vertically compound structure might happen not to have any horizontal breaks. For that situation, both IsVerticallyCompound and this method will return true.

# See Also

[CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)