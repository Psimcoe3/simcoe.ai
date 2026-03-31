[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetComparisonResult Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

An enumerated type listing all the relationship types between two sets of arbitrary nature.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public enum SetComparisonResult ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration SetComparisonResult ``` |

 

| Visual C++ |
| --- |
| ``` public enum class SetComparisonResult ``` |

# Members

| Member name | Description |
| --- | --- |
| LeftEmpty | The left set is empty and the right set is not. |
| RightEmpty | The right set is empty and the left set is not. |
| BothEmpty | Both sets are empty. |
| Disjoint | Both sets are not empty and don't overlap. |
| Overlap | The overlap of two sets is not empty and strict subset of both. |
| Subset | Both sets are not empty and the left set is strict subset of the right. |
| Superset | Both sets are not empty and the left set is strict superset of the right. |
| Equal | Two nonempty sets are equal. |

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)