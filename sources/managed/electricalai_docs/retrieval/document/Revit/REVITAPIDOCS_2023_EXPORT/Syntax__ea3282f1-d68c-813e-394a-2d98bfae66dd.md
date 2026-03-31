[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsActive Method

---



|  |
| --- |
| [FailuresAccessor Class](dea68b06-a061-fc05-d814-db741f2e7f14.htm)   [See Also](#seeAlsoToggle) |

Method allows to check if this instance of the accessor is currently active.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public bool IsActive() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsActive As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsActive() ``` |

#### Return Value

True if this instance is currently active and can be used.

# Remarks

Generally, this instance is active when it is passed to any of interfaces used in the process of failure resolution, and becomes inactive after returning control to Revit. The only special case is if failures processor returns WaitForUserInput, in which case document stays in the FailureMode and instance of failures accessor stays active till FailureMode is ended.

# See Also

[FailuresAccessor Class](dea68b06-a061-fc05-d814-db741f2e7f14.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)