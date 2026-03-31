[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetIsLeaderVisible Method

---



|  |
| --- |
| [IndependentTag Class](e52073e2-9d98-6fb5-eb43-288cf9ed2e28.htm)   [See Also](#seeAlsoToggle) |

Set tag's leader that points to specified reference to be visible or not. This option can be set only if the LeadersPresentationMode is ShowSpecificLeaders.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public void SetIsLeaderVisible( 	Reference referenceTagged, 	bool visible ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetIsLeaderVisible ( _ 	referenceTagged As Reference, _ 	visible As Boolean _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetIsLeaderVisible( 	Reference^ referenceTagged,  	bool visible ) ``` |

#### Parameters

referenceTagged
:   Type:  [Autodesk.Revit.DB Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)    
     The reference which is tagged.

visible
:   Type:  System Boolean    
     True for showing the leader, false to hide it.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The specified reference is not currently tagged. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The LeadersPresentationMode should be set to ShowSpecificLeaders. |

# See Also

[IndependentTag Class](e52073e2-9d98-6fb5-eb43-288cf9ed2e28.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)