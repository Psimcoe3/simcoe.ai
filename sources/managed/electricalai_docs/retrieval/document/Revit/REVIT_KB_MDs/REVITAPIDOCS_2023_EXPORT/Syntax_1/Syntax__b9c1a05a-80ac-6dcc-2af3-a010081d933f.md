[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddResolution Method

---



|  |
| --- |
| [FailureMessage Class](d0795bd6-f092-90f2-5c2c-3876e616454c.htm)   [See Also](#seeAlsoToggle) |

Adds a resolution for the failure.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public FailureMessage AddResolution( 	FailureResolutionType type, 	FailureResolution resolution ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function AddResolution ( _ 	type As FailureResolutionType, _ 	resolution As FailureResolution _ ) As FailureMessage ``` |

 

| Visual C++ |
| --- |
| ``` public: FailureMessage^ AddResolution( 	FailureResolutionType type,  	FailureResolution^ resolution ) ``` |

#### Parameters

type
:   Type:  [Autodesk.Revit.DB FailureResolutionType](786e6422-f66d-5320-99f9-e530819e50a1.htm)    
     The type of the resolution.

resolution
:   Type:  [Autodesk.Revit.DB FailureResolution](8075460b-afbf-6558-b402-b1f75fdf2412.htm)    
     The resolution.

#### Return Value

The FailureMessage.

# Remarks

Each pair of FailureResolutionType and FailureResolution must have been defined in FailureDefinition, and could only be added once.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | type is not a valid resolution type for this FailureMessage. -or- resolution of type is not valid for this FailureMessage. -or- This FailureMessage already contains a resolution of type type. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This FailureMessage is already posted to a document |

# See Also

[FailureMessage Class](d0795bd6-f092-90f2-5c2c-3876e616454c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)