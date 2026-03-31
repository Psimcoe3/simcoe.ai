[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SortParameters Method

---



|  |
| --- |
| [GlobalParametersManager Class](f3af05ec-1f0c-fe86-6708-0a211a40bcda.htm)   [See Also](#seeAlsoToggle) |

Sorts global parameters in the desired order.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public static void SortParameters( 	Document document, 	ParametersOrder order ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Sub SortParameters ( _ 	document As Document, _ 	order As ParametersOrder _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: static void SortParameters( 	Document^ document,  	ParametersOrder order ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     Document containing the global parameters to be sorted

order
:   Type:  [Autodesk.Revit.DB ParametersOrder](771bd717-9d4d-d36d-0948-94e2e73f392c.htm)    
     Desired sorting order

# Remarks

All global parameters are sorted, but only within the range of their respective parameter group.

This operation has no effect on the global parameters themselves. The sorted order is only visible in the standard Global Parameters dialog. However, the order of parameters is serialized in the document, thus available on the DB level as well.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Global parameters are not supported in the given document. A possible cause is that it is not a project document, for global parameters are not supported in Revit families. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[GlobalParametersManager Class](f3af05ec-1f0c-fe86-6708-0a211a40bcda.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)