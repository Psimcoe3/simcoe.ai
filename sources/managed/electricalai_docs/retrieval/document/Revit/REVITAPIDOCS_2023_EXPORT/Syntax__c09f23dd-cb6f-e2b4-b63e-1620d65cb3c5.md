[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetDistributionPath Method

---



|  |
| --- |
| [RebarHandlePositionData Class](de2e3a20-4203-f6bd-8166-a0d3a973d16b.htm)   [See Also](#seeAlsoToggle) |

Gets the distribution path currently stored in the rebar.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public IList<Curve> GetDistributionPath() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetDistributionPath As IList(Of Curve) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<Curve^>^ GetDistributionPath() ``` |

#### Return Value

Returns array of curves that represent the distribution path.

# Remarks

For a free form rebar set the distance between two consecutive bars may be different if it is calculated between different points on bars. The distribution path is an array of curves with the property that based on these curves the set was calculated to respect the layout rule and number of bars or spacing.

# See Also

[RebarHandlePositionData Class](de2e3a20-4203-f6bd-8166-a0d3a973d16b.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)