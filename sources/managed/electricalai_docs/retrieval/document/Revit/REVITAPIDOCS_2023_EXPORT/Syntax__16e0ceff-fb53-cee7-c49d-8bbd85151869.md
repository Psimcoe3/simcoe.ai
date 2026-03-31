[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarBendData Constructor (RebarBarType, RebarHookType, RebarHookType, RebarStyle, RebarHookOrientation, RebarHookOrientation)

---



|  |
| --- |
| [RebarBendData Class](027b5619-ad82-74b3-1d78-efe86a1ef96b.htm)   [See Also](#seeAlsoToggle) |

Constructs a new RebarBendData using the bar type, hook types, style and orientation values.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public RebarBendData( 	RebarBarType barType, 	RebarHookType hookType0, 	RebarHookType hookType1, 	RebarStyle style, 	RebarHookOrientation hookOrient0, 	RebarHookOrientation hookOrient1 ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	barType As RebarBarType, _ 	hookType0 As RebarHookType, _ 	hookType1 As RebarHookType, _ 	style As RebarStyle, _ 	hookOrient0 As RebarHookOrientation, _ 	hookOrient1 As RebarHookOrientation _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: RebarBendData( 	RebarBarType^ barType,  	RebarHookType^ hookType0,  	RebarHookType^ hookType1,  	RebarStyle style,  	RebarHookOrientation hookOrient0,  	RebarHookOrientation hookOrient1 ) ``` |

#### Parameters

barType
:   Type:  [Autodesk.Revit.DB.Structure RebarBarType](467b44cc-54e7-3ecf-07e1-ad15d05fe800.htm)

hookType0
:   Type:  [Autodesk.Revit.DB.Structure RebarHookType](3c7a78d5-f92b-e58b-e7c9-7927537498fd.htm)

hookType1
:   Type:  [Autodesk.Revit.DB.Structure RebarHookType](3c7a78d5-f92b-e58b-e7c9-7927537498fd.htm)

style
:   Type:  [Autodesk.Revit.DB.Structure RebarStyle](a9ac65a6-29e6-25e5-caca-502e21385f47.htm)

hookOrient0
:   Type:  [Autodesk.Revit.DB.Structure RebarHookOrientation](e8365754-0811-8d4e-864a-55bf34af3a87.htm)

hookOrient1
:   Type:  [Autodesk.Revit.DB.Structure RebarHookOrientation](e8365754-0811-8d4e-864a-55bf34af3a87.htm)

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[RebarBendData Class](027b5619-ad82-74b3-1d78-efe86a1ef96b.htm)

[RebarBendData Overload](4d1aabbd-79b2-617f-151b-2e4097c8a4d5.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)