[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidState Method

---



|  |
| --- |
| [TemporaryViewModes Class](cf6ecc84-e459-55c5-a4d7-d88ae4033a23.htm)   [See Also](#seeAlsoToggle) |

Tests whether the given state is valid for the associated view and the context the view is currently in.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016 Subscription Update

# Syntax

| C# |
| --- |
| ``` public bool IsValidState( 	PreviewFamilyVisibilityMode state ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsValidState ( _ 	state As PreviewFamilyVisibilityMode _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsValidState( 	PreviewFamilyVisibilityMode state ) ``` |

#### Parameters

state
:   Type:  [Autodesk.Revit.DB PreviewFamilyVisibilityMode](efc5a721-5885-f63e-64af-83e0c93e6c45.htm)    
     A state of the PreviewFamilyVisibilityMode

#### Return Value

Returns True if the state is applicable for the view; False otherwise.

# Remarks

As long as the PreviewFamilyVisibility mode is available and enabled in the associated view, the  *Off*  and  *On*  states are always valid. However, the  *Uncut*  state is only valid in plan views and reflected ceilings.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[TemporaryViewModes Class](cf6ecc84-e459-55c5-a4d7-d88ae4033a23.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)