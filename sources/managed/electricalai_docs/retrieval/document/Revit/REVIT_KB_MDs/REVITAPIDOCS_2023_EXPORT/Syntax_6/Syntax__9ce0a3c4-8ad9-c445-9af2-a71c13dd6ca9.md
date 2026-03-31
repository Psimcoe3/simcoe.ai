[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetFacet Method

---



|  |
| --- |
| [PolymeshTopology Class](fef5982c-3825-eed0-f792-1e0bff5509c2.htm)   [See Also](#seeAlsoToggle) |

Returns a definition of one facet

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public PolymeshFacet GetFacet( 	int idx ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetFacet ( _ 	idx As Integer _ ) As PolymeshFacet ``` |

 

| Visual C++ |
| --- |
| ``` public: PolymeshFacet^ GetFacet( 	int idx ) ``` |

#### Parameters

idx
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     A zero-based index of the facet

#### Return Value

An instance of PolymeshFacet that represents one facet defined by 3 vertices of the polymesh.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given value is not a valid index of a facet of the polymesh. A valid value is not negative and is smaller than the number of facets in the polymesh. |

# See Also

[PolymeshTopology Class](fef5982c-3825-eed0-f792-1e0bff5509c2.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)