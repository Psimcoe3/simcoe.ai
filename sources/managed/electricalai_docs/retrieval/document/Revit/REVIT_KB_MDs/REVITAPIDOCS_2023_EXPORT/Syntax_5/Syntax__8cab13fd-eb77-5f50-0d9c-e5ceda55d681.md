[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetFilters Method

---



|  |
| --- |
| [ElementLogicalFilter Class](3b8d6b55-0cab-1810-1188-840800e5eaa2.htm)   [See Also](#seeAlsoToggle) |

Replaces current filters in the logical filter with any number of input filters.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2020

# Syntax

| C# |
| --- |
| ``` public void SetFilters( 	IList<ElementFilter> filters ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetFilters ( _ 	filters As IList(Of ElementFilter) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetFilters( 	IList<ElementFilter^>^ filters ) ``` |

#### Parameters

filters
:   Type:  System.Collections.Generic IList   [ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)    
     A collection of input filters.

# Remarks

The input filters will be copied.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The filter collection is empty, or contains invalid inputs. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ElementLogicalFilter Class](3b8d6b55-0cab-1810-1188-840800e5eaa2.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)