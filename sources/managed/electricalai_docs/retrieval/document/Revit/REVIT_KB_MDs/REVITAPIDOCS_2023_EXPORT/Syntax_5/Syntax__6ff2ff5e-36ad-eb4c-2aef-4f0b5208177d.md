[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetLocationPathForStraightRun Method

---



|  |
| --- |
| [StairsRun Class](ea0e49a0-a007-79d0-c902-a24b1359ae28.htm)   [See Also](#seeAlsoToggle) |

Set location path for a straight run by giving a line.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static bool SetLocationPathForStraightRun( 	StairsRun stairsRun, 	Line locationPath ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function SetLocationPathForStraightRun ( _ 	stairsRun As StairsRun, _ 	locationPath As Line _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool SetLocationPathForStraightRun( 	StairsRun^ stairsRun,  	Line^ locationPath ) ``` |

#### Parameters

stairsRun
:   Type:  [Autodesk.Revit.DB.Architecture StairsRun](ea0e49a0-a007-79d0-c902-a24b1359ae28.htm)    
     The run whose location path will be set.

locationPath
:   Type:  [Autodesk.Revit.DB Line](e7329450-434a-918b-661c-65e15e0585a5.htm)    
     The location path.

#### Return Value

Indicate if set is success or not.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The input locationPath is not a bound line. -or- The input locationPath is not a valid location path line for straight run. -or- The locationPath is not valid line used as stairs path(probably it's too short). |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The stairs element represented by stairsRun is not in an active StairsEditScope. The run cannot be modified. |
| [Autodesk.Revit.Exceptions RegenerationFailedException](787bb389-74c2-5ce7-cdd6-32211209ded2.htm) | The locationPath doesn't satisfy restrictions to generate straight run. |

# See Also

[StairsRun Class](ea0e49a0-a007-79d0-c902-a24b1359ae28.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)