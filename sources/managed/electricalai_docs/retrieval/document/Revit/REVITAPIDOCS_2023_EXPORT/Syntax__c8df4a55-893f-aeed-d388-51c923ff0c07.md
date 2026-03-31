[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AnalysisForClosedLoopHydronicPipingNetworks Property

---



|  |
| --- |
| [PipeSettings Class](2de0109b-0d0d-a0fe-2adf-6edec8bc1a06.htm)   [See Also](#seeAlsoToggle) |

Indicates whether to enable analysis for closed loop hydronic piping networks.

**Namespace:**   [Autodesk.Revit.DB.Plumbing](cc553597-37c2-fcd9-6025-d904c129c80a.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public bool AnalysisForClosedLoopHydronicPipingNetworks { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property AnalysisForClosedLoopHydronicPipingNetworks As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool AnalysisForClosedLoopHydronicPipingNetworks { 	bool get (); 	void set (bool value); } ``` |

# Remarks

For closed loop hydronic piping networks, Revit can analyze flow and pressure values for supply and return loops. In the model, select a pump to see the results of the analysis in the Properties palette.

A closed loop hydronic piping network must contain:

A single pump/circulatorA single source, such as a boilerMultiple piping segmentsMultiple terminals, such as radiators.

A network may contain a direct return loop or a reverse return loop.

# See Also

[PipeSettings Class](2de0109b-0d0d-a0fe-2adf-6edec8bc1a06.htm)

[Autodesk.Revit.DB.Plumbing Namespace](cc553597-37c2-fcd9-6025-d904c129c80a.htm)