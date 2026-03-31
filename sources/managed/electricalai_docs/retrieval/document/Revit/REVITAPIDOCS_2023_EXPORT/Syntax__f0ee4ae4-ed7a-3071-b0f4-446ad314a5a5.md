[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetSketchCurves Method

---



|  |
| --- |
| [RevisionCloud Class](43bdb2c4-2b9c-e3fa-4d6a-8c9970a9f7b6.htm)   [See Also](#seeAlsoToggle) |

Returns copies of the Curves that form this RevisionCloud.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public IList<Curve> GetSketchCurves() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetSketchCurves As IList(Of Curve) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<Curve^>^ GetSketchCurves() ``` |

#### Return Value

Copies of the sketched curves that form this RevisionCloud.

# Remarks

Note that there is no requirement that the curves form closed loops or avoid self-intersections. The curves may also form multiple closed loops.

# See Also

[RevisionCloud Class](43bdb2c4-2b9c-e3fa-4d6a-8c9970a9f7b6.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)