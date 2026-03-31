[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetHostIds Method

---



|  |
| --- |
| [WallSweep Class](8edb03ef-dc10-04d8-d8ea-6342e4a2185b.htm)   [See Also](#seeAlsoToggle) |

Gets a list of all host walls on which the sweep resides.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public IList<ElementId> GetHostIds() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetHostIds As IList(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<ElementId^>^ GetHostIds() ``` |

#### Return Value

The list of wall ids.

# Remarks

Fixed wall sweeps from vertically compound structures will return only one host element.

# See Also

[WallSweep Class](8edb03ef-dc10-04d8-d8ea-6342e4a2185b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)