[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddRule Method (RoutingPreferenceRuleGroupType, RoutingPreferenceRule, Int32)

---



|  |
| --- |
| [RoutingPreferenceManager Class](a8300b97-72a6-beb5-733b-ec4cfea6c472.htm)   [See Also](#seeAlsoToggle) |

Adds a new routing preference rule to the specified position in the rule group.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public void AddRule( 	RoutingPreferenceRuleGroupType groupType, 	RoutingPreferenceRule rule, 	int index ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub AddRule ( _ 	groupType As RoutingPreferenceRuleGroupType, _ 	rule As RoutingPreferenceRule, _ 	index As Integer _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void AddRule( 	RoutingPreferenceRuleGroupType groupType,  	RoutingPreferenceRule^ rule,  	int index ) ``` |

#### Parameters

groupType
:   Type:  [Autodesk.Revit.DB RoutingPreferenceRuleGroupType](79896fd9-e90c-6561-3bc4-7cefd4692ae5.htm)    
     The routing preference group type in which the rule should be added.

rule
:   Type:  [Autodesk.Revit.DB RoutingPreferenceRule](28dd1a35-5115-c0fb-26e3-7bce14893b89.htm)    
     The new rule to be added.

index
:   Type:  System Int32    
     The zero-based index position where the new rule will be added.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | index is not a valid zero-based index within groupType. -or- The rule cannot be added to the groupType. -or- Thrown if the index is out of bounds, or the rule is not valid for this group (e.g. an elbow may not be added to the junction group). |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Mechanical Electrical Piping. |

# See Also

[RoutingPreferenceManager Class](a8300b97-72a6-beb5-733b-ec4cfea6c472.htm)

[AddRule Overload](06817419-419d-35bf-8538-3584e415a1c4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)