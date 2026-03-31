[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ReplaceFailures Method

---



|  |
| --- |
| [FailuresAccessor Class](dea68b06-a061-fc05-d814-db741f2e7f14.htm)   [See Also](#seeAlsoToggle) |

Deletes all failure messages currently posted in a document and replaces them with one "generic" failure.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public void ReplaceFailures( 	FailureMessage failure ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub ReplaceFailures ( _ 	failure As FailureMessage _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void ReplaceFailures( 	FailureMessage^ failure ) ``` |

#### Parameters

failure
:   Type:  [Autodesk.Revit.DB FailureMessage](d0795bd6-f092-90f2-5c2c-3876e616454c.htm)    
     FailureMessage that should replace all currently posted messages. It must have severity DocumentCorruption.

# Remarks

If analysis done by Failures Processing code concludes that in a given context delivering of the posted failures to the user makes no sense, this method can be used to discard all posted failures and substitute one "generic" one, that will be delivered to the user and then transaction forced to be aborted. After the call, (pre)processing of failures should return ProceedWithRollback.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Severity of failure must be FailureSeverity::DocumentCorruption. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This FailuresAccessor is inactive (is used outside of failures processing). |

# See Also

[FailuresAccessor Class](dea68b06-a061-fc05-d814-db741f2e7f14.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)