[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RemoveMemberIds Method

---



|  |
| --- |
| [AssemblyInstance Class](4e60704c-dfe3-72b6-7892-6440503fa078.htm)   [See Also](#seeAlsoToggle) |

Removes member element ids from the assembly instance.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public void RemoveMemberIds( 	ICollection<ElementId> memberIds ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub RemoveMemberIds ( _ 	memberIds As ICollection(Of ElementId) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void RemoveMemberIds( 	ICollection<ElementId^>^ memberIds ) ``` |

#### Parameters

memberIds
:   Type:  System.Collections.Generic ICollection   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Element ids to be removed from the assembly instance.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | One or more element ids was not permitted to be removed from the assembly instance. Provided set should not be empty and all elements should be a member of the assembly instance. -or- The provided set includes one or more element ids that cannot be added to or removed from the assembly on their own. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[AssemblyInstance Class](4e60704c-dfe3-72b6-7892-6440503fa078.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)