[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CurveElementFilter Constructor (CurveElementType, Boolean)

---



|  |
| --- |
| [CurveElementFilter Class](d31574f5-4400-c4f9-04dd-4418c302e3c5.htm)   [See Also](#seeAlsoToggle) |

Constructs a new instance of a filter to match specific types of curve elements, with the option to match all curves which are not of the given curve type.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public CurveElementFilter( 	CurveElementType curveElementType, 	bool inverted ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	curveElementType As CurveElementType, _ 	inverted As Boolean _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: CurveElementFilter( 	CurveElementType curveElementType,  	bool inverted ) ``` |

#### Parameters

curveElementType
:   Type:  [Autodesk.Revit.DB CurveElementType](bb7da2a1-6a68-df2a-aacb-1d90c8a0f5b7.htm)    
     The curve element type to match.

inverted
:   Type:  [System Boolean](http://msdn2.microsoft.com/en-us/library/a28wyd50)    
     True if the filter should match all curves which are not of the given curve type.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[CurveElementFilter Class](d31574f5-4400-c4f9-04dd-4418c302e3c5.htm)

[CurveElementFilter Overload](2a935b32-7766-c774-b4b0-6db61bffc4d0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)