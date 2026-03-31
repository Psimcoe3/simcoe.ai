[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RemoveRule Method

---



|  |
| --- |
| [RoutingPreferenceManager Class](a8300b97-72a6-beb5-733b-ec4cfea6c472.htm)   [See Also](#seeAlsoToggle) |

Removes an existing routing preference rule. Thrown if the index is out of bounds.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public void RemoveRule( 	RoutingPreferenceRuleGroupType groupType, 	int index ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub RemoveRule ( _ 	groupType As RoutingPreferenceRuleGroupType, _ 	index As Integer _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void RemoveRule( 	RoutingPreferenceRuleGroupType groupType,  	int index ) ``` |

#### Parameters

groupType
:   Type:  [Autodesk.Revit.DB RoutingPreferenceRuleGroupType](79896fd9-e90c-6561-3bc4-7cefd4692ae5.htm)    
     The routing preference group type in which the rule should be removed.

index
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The index position of removed routing preference rule in the group.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | index is not a valid zero-based index within groupType. -or- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Mechanical Electrical Piping. |

# See Also

[RoutingPreferenceManager Class](a8300b97-72a6-beb5-733b-ec4cfea6c472.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)