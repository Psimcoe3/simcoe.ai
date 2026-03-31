[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetReleaseType Method

---



|  |
| --- |
| [AnalyticalMember Class](57c87ac5-a82e-5c7e-2f06-6dbf1f697566.htm)   [See Also](#seeAlsoToggle) |

Sets the release type.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public void SetReleaseType( 	bool start, 	ReleaseType releaseType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetReleaseType ( _ 	start As Boolean, _ 	releaseType As ReleaseType _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetReleaseType( 	bool start,  	ReleaseType releaseType ) ``` |

#### Parameters

start
:   Type:  System Boolean    
     The position on Analytical Member element. True for start, false for end.

releaseType
:   Type:  [Autodesk.Revit.DB.Structure ReleaseType](29394540-619a-61e0-abc2-449dc868e246.htm)    
     The type of release.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[AnalyticalMember Class](57c87ac5-a82e-5c7e-2f06-6dbf1f697566.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)