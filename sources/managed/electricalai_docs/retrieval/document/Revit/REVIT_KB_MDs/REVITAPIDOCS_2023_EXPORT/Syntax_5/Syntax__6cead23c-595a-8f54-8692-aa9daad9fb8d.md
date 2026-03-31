[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PlanTopologies Property (Phase)

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [See Also](#seeAlsoToggle) |

Gets the PlanTopologies of the current project in a given phase.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public PlanTopologySet this[ 	Phase phase ] { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property PlanTopologies ( _ 	phase As Phase _ ) As PlanTopologySet 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property PlanTopologySet^ PlanTopologies[Phase^ phase] { 	PlanTopologySet^ get (Phase^ phase); } ``` |

#### Parameters

phase
:   Type:  [Autodesk.Revit.DB Phase](ab01f390-a8e8-c21c-b2d0-6dd21056cdec.htm)    
     The phase of the Plan Topology.

# Remarks

Accessing plan topologies requires that document is modifiable as it will actually trigger calculating plan topologies if they have not been calculated yet. The time necessary for the calculations may be significant and should be considered.

# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[PlanTopologies Overload](2494d273-3525-f04d-b20d-d346c402a99d.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)