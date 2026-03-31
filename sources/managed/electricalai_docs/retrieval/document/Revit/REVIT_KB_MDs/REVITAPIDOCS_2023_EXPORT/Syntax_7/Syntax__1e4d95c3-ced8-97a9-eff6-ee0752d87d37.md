[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Close Method

---



|  |
| --- |
| [WorksetConfiguration Class](eefef6f4-0892-4bb5-8840-5e99aebc65c9.htm)   [See Also](#seeAlsoToggle) |

Sets a group of user-created worksets to close.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public void Close( 	IList<WorksetId> worksetsToClose ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub Close ( _ 	worksetsToClose As IList(Of WorksetId) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void Close( 	IList<WorksetId^>^ worksetsToClose ) ``` |

#### Parameters

worksetsToClose
:   Type:  System.Collections.Generic IList   [WorksetId](8bece327-c269-8101-b4c2-38632f593fe6.htm)    
     The group of user-created worksets to close. Non-user-created worksets and invalid workset ids will be ignored.

# Remarks

Calling this method on a configuration created with options other than WorksetConfigurationOption.CloseAllWorksets will set these worksets to be explicitly closed. If all worksets are set to close, the configuration will be unchanged. Worksets other than the inputs are unaffected.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[WorksetConfiguration Class](eefef6f4-0892-4bb5-8840-5e99aebc65c9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)