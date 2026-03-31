[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WallSweepOrientation Property

---



|  |
| --- |
| [WallSweepInfo Class](140876fa-4c17-ad27-8a12-a4bf755e06f3.htm)   [See Also](#seeAlsoToggle) |

Indicates how the profile of a horiztonal sweep is oriented with repect to the wall side face.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public WallSweepOrientation WallSweepOrientation { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property WallSweepOrientation As WallSweepOrientation 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property WallSweepOrientation WallSweepOrientation { 	WallSweepOrientation get (); 	void set (WallSweepOrientation value); } ``` |

#### Field Value

Allowed values are Horizontal and Perpendicular. Default is Perpendicular

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[WallSweepInfo Class](140876fa-4c17-ad27-8a12-a4bf755e06f3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)