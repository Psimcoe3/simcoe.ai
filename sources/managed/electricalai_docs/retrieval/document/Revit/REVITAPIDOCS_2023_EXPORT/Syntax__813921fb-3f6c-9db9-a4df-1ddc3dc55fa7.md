[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetNonContinuousRail Method

---



|  |
| --- |
| [NonContinuousRailStructure Class](a47d9f99-df86-e25b-d24f-635362d065b6.htm)   [See Also](#seeAlsoToggle) |

Gets the Non-Continuous Rail object of specified index from the Rail Structure.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 19.0.0.0 (19.0.0.405)   
  **Since:**  2019

# Syntax

| C# |
| --- |
| ``` public NonContinuousRailInfo GetNonContinuousRail( 	int index ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetNonContinuousRail ( _ 	index As Integer _ ) As NonContinuousRailInfo ``` |

 

| Visual C++ |
| --- |
| ``` public: NonContinuousRailInfo^ GetNonContinuousRail( 	int index ) ``` |

#### Parameters

index
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     Non-Continuous Rail index.

#### Return Value

The requested object handle.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The index index is out of range. |

# See Also

[NonContinuousRailStructure Class](a47d9f99-df86-e25b-d24f-635362d065b6.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)