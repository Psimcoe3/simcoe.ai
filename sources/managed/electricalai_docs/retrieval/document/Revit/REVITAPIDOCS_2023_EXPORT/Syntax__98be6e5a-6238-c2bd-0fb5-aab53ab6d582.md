[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### OfKind Method

---



|  |
| --- |
| [FilteredWorksetCollector Class](30e91d82-33a2-2561-db2a-28098a96b3ec.htm)   [See Also](#seeAlsoToggle) |

Applies a WorksetKindFilter to the collector.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public FilteredWorksetCollector OfKind( 	WorksetKind worksetKind ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function OfKind ( _ 	worksetKind As WorksetKind _ ) As FilteredWorksetCollector ``` |

 

| Visual C++ |
| --- |
| ``` public: FilteredWorksetCollector^ OfKind( 	WorksetKind worksetKind ) ``` |

#### Parameters

worksetKind
:   Type:  [Autodesk.Revit.DB WorksetKind](b1e116b1-2ca0-61c1-533d-4a06e38e335d.htm)    
     The WorksetKind of the workset.

#### Return Value

A handle to this collector. This is the same collector that has just been modified, returned so you can chain multiple calls together in one line.

# Remarks

Only worksets whose WorksetKind is an exact match to the input WorksetKind will pass the collector.

If you have an active iterator to this collector it will be stopped by this call.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[FilteredWorksetCollector Class](30e91d82-33a2-2561-db2a-28098a96b3ec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)