[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetOffset Method

---



|  |
| --- |
| [PlanViewRange Class](7edc5f13-a5fa-5c7a-9a03-ac6cbed1f005.htm)   [See Also](#seeAlsoToggle) |

Set the offset value associated with a View Depth plane

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public void SetOffset( 	PlanViewPlane planViewPlane, 	double offset ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetOffset ( _ 	planViewPlane As PlanViewPlane, _ 	offset As Double _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetOffset( 	PlanViewPlane planViewPlane,  	double offset ) ``` |

#### Parameters

planViewPlane
:   Type:  [Autodesk.Revit.DB PlanViewPlane](80d20187-97ea-f6c0-a3a8-d5545e0b3863.htm)    
     View Depth plane

offset
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Offset value

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[PlanViewRange Class](7edc5f13-a5fa-5c7a-9a03-ac6cbed1f005.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)