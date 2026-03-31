[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsLeaderValid Method

---



|  |
| --- |
| [DatumPlane Class](3e0a6725-ee40-c4d5-839f-b7720c1fe2af.htm)   [See Also](#seeAlsoToggle) |

Identifies if the leader valid or not for this DatumPlane. This method does not apply to Reference planes (which do not support leaders).

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public bool IsLeaderValid( 	DatumEnds datumEnd, 	View view, 	Leader leader ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsLeaderValid ( _ 	datumEnd As DatumEnds, _ 	view As View, _ 	leader As Leader _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsLeaderValid( 	DatumEnds datumEnd,  	View^ view,  	Leader^ leader ) ``` |

#### Parameters

datumEnd
:   Type:  [Autodesk.Revit.DB DatumEnds](60cdd5d4-8c6c-320b-7b8b-1cc4487edd9c.htm)    
     The end of the datum plane.

view
:   Type:  [Autodesk.Revit.DB View](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)    
     The view on which the DatumPlane shows.

leader
:   Type:  [Autodesk.Revit.DB Leader](66228564-d8b8-fc81-454c-e175528f7188.htm)    
     The Leader for setting the datum plane.

#### Return Value

True if the leader is valid for set leader, false otherwise.

# Remarks

If the view or leader is null, it will throw ArgumentNullException; A valid leader meets the following conditions:

* The leader's End, Elbow and Anchor should lie in the View's plane
* The End of the leader should be on the datum plane's curve(s)
* The Elbow of the leader should be between the End and Anchor

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This datum plane has no leaders. -or- The DatumPlane should not have a leader. |

# See Also

[DatumPlane Class](3e0a6725-ee40-c4d5-839f-b7720c1fe2af.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)