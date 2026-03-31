[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetRuleId Method

---



|  |
| --- |
| [PerformanceAdviser Class](f9b0b017-f98f-79a3-ce7b-b1c867bb22f2.htm)   [See Also](#seeAlsoToggle) |

Retrieves an id of a rule for a given index in the list.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public PerformanceAdviserRuleId GetRuleId( 	int index ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetRuleId ( _ 	index As Integer _ ) As PerformanceAdviserRuleId ``` |

 

| Visual C++ |
| --- |
| ``` public: PerformanceAdviserRuleId^ GetRuleId( 	int index ) ``` |

#### Parameters

index
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The index to retrieve the rule id for.

#### Return Value

The rule id.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The index is outside of acceptable range. |

# See Also

[PerformanceAdviser Class](f9b0b017-f98f-79a3-ce7b-b1c867bb22f2.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)