[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetPhaseStatusPresentation Method

---



|  |
| --- |
| [PhaseFilter Class](3236c80e-48be-f657-951f-70490a43f065.htm)   [See Also](#seeAlsoToggle) |

Gets the phase status presentation.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public PhaseStatusPresentation GetPhaseStatusPresentation( 	ElementOnPhaseStatus status ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetPhaseStatusPresentation ( _ 	status As ElementOnPhaseStatus _ ) As PhaseStatusPresentation ``` |

 

| Visual C++ |
| --- |
| ``` public: PhaseStatusPresentation GetPhaseStatusPresentation( 	ElementOnPhaseStatus status ) ``` |

#### Parameters

status
:   Type:  [Autodesk.Revit.DB ElementOnPhaseStatus](bfc481cc-11c8-de0b-1d71-7b2ffa711780.htm)    
     The element phase status.

#### Return Value

The phase status presentation.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | status is invalid for presentation query. |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[PhaseFilter Class](3236c80e-48be-f657-951f-70490a43f065.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)