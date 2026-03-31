[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LeaderShape Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

Supported geometric shapes of annotation leaders.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public enum LeaderShape ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration LeaderShape ``` |

 

| Visual C++ |
| --- |
| ``` public enum class LeaderShape ``` |

# Members

| Member name | Description |
| --- | --- |
| Straight | A single straight line between the end point and anchor point. |
| Kinked | A kinked line with a shoulder defined by an elbow point. |
| Arc | An arc between between the end point and anchor point. In this shape the elbow point controls the arc's radius. |

# Remarks

Although the  [Leader](66228564-d8b8-fc81-454c-e175528f7188.htm)  class supports all available shapes, not all types of leaders may have the option to change its shape. For example, leaders of text annotations can be of any shape, while leaders of level lines are never curved.

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)