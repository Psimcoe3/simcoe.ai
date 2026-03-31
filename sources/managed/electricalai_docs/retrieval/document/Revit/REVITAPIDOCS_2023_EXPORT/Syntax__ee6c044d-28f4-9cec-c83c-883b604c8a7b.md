[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ResolveFailure Method

---



|  |
| --- |
| [FailuresAccessor Class](dea68b06-a061-fc05-d814-db741f2e7f14.htm)   [See Also](#seeAlsoToggle) |

Resolves one failure using the failure resolution type last set for it.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public void ResolveFailure( 	FailureMessageAccessor failure ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub ResolveFailure ( _ 	failure As FailureMessageAccessor _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void ResolveFailure( 	FailureMessageAccessor^ failure ) ``` |

#### Parameters

failure
:   Type:  [Autodesk.Revit.DB FailureMessageAccessor](753477d8-b720-97a0-26f5-439d49de418c.htm)    
     The accessor to the failure to be resolved.

# Remarks

If failure resolution type was not set, the default failure resolution type will be used. After execution of the failure resolution the failure will not be removed from the document automatically. To prevent the failure from being delivered to the user, failures (pre)processor should return ProceedWithCommit. It will cause failures to be regenerated and failure resolution process to be restarted. If attempt to resolve failure was not successful, and the same failure is present on repetitive calls of the failures (pre)processor, the preprocessor code should take care to attempt a different resolution the next time the failure appears, to avoid an infinite loop.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | failure has not been properly initialized. -or- failure does not have any resolutions. -or- Default resolution of failure is not permitted or not applicable. -or- The failure was already attempted to resolve twice with that resolution type. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This FailuresAccessor is inactive (is used outside of failures processing). -or- Resolution of failures is not permitted in the current state of the document. |

# See Also

[FailuresAccessor Class](dea68b06-a061-fc05-d814-db741f2e7f14.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)