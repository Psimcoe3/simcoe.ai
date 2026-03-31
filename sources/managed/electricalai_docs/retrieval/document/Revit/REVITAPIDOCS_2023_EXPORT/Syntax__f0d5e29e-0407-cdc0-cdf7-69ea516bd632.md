[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LeadersPresentationMode Property

---



|  |
| --- |
| [IndependentTag Class](e52073e2-9d98-6fb5-eb43-288cf9ed2e28.htm)   [See Also](#seeAlsoToggle) |

Identifies the Presentation Mode that is applied to tag leaders.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public LeadersPresentationMode LeadersPresentationMode { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property LeadersPresentationMode As LeadersPresentationMode 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property LeadersPresentationMode LeadersPresentationMode { 	LeadersPresentationMode get (); 	void set (LeadersPresentationMode value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The LeadersPresentationMode LeadersPresentationMode.ShowOnlyOne or LeadersPresentationMode.ShowSpecificLeaders can't be set to a tag with only one leader. |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | When setting this property: For this tag leaders are not allowed. |

# See Also

[IndependentTag Class](e52073e2-9d98-6fb5-eb43-288cf9ed2e28.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)