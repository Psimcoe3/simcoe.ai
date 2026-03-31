[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsRuleEnabled Method (Int32)

---



|  |
| --- |
| [PerformanceAdviser Class](f9b0b017-f98f-79a3-ce7b-b1c867bb22f2.htm)   [See Also](#seeAlsoToggle) |

Retrieves an enabled/disabled status for the given rule.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public bool IsRuleEnabled( 	int index ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsRuleEnabled ( _ 	index As Integer _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsRuleEnabled( 	int index ) ``` |

#### Parameters

index
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The rule index to retrieve enabled/disabled status for.

#### Return Value

True if rule is disabled, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The index is outside of acceptable range. |

# See Also

[PerformanceAdviser Class](f9b0b017-f98f-79a3-ce7b-b1c867bb22f2.htm)

[IsRuleEnabled Overload](a4b32b23-c467-c6a7-0497-858b34a42d83.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)