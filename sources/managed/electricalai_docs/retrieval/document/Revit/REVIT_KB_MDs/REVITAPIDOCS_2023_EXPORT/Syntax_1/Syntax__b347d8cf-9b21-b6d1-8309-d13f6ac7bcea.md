[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MoveParameterUpOrder Method

---



|  |
| --- |
| [GlobalParametersManager Class](f3af05ec-1f0c-fe86-6708-0a211a40bcda.htm)   [See Also](#seeAlsoToggle) |

Moves given paramerer Up in the current order.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public static bool MoveParameterUpOrder( 	Document document, 	ElementId parameterId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function MoveParameterUpOrder ( _ 	document As Document, _ 	parameterId As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool MoveParameterUpOrder( 	Document^ document,  	ElementId^ parameterId ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     Document containing the give global parameter

parameterId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The parameter to move up

#### Return Value

Indicates whether the parameter could be moved Up in order or not.

# Remarks

A parameter can only be moved within its parameter group, meaning that repeated moving a parameter will not push the parameter out of and into the next (in order) parameter group. When a parameter can no longer move because it is at the boundary of its group, this method returns False.

This operation has no effect on the global parameters themselves. The rearranged order is only visible in the standard Global Parameters dialog. However, the order of parameters is serialized in the document, thus available on the DB level as well.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Global parameters are not supported in the given document. A possible cause is that it is not a project document, for global parameters are not supported in Revit families. -or- The input parameterId is not of a valid global parameter of the given document. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[GlobalParametersManager Class](f3af05ec-1f0c-fe86-6708-0a211a40bcda.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)