[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateHydraulicSeparation Method

---



|  |
| --- |
| [PipingSystem Class](6abbdfa2-69a5-eef1-2663-89a5faf91831.htm)   [See Also](#seeAlsoToggle) |

Creates new system which is hydraulically separated from the existing system.

**Namespace:**   [Autodesk.Revit.DB.Plumbing](cc553597-37c2-fcd9-6025-d904c129c80a.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2019

# Syntax

| C# |
| --- |
| ``` public static ISet<ElementId> CreateHydraulicSeparation( 	Document document, 	ISet<ElementId> pipeElementIds ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateHydraulicSeparation ( _ 	document As Document, _ 	pipeElementIds As ISet(Of ElementId) _ ) As ISet(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: static ISet<ElementId^>^ CreateHydraulicSeparation( 	Document^ document,  	ISet<ElementId^>^ pipeElementIds ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document where the new system is created.

pipeElementIds
:   Type:  System.Collections.Generic ISet   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The boundary pipe that defines a new system. Multiple pipes are allowed to create more than one separated systems.

#### Return Value

The newly created piping system elements.

# Remarks

Hydraulically separated systems allow independent flow and pressure analysis for each hydraulic loop. For example, each hydraulic loop has its own cirtical path. The calculated pressure drop on the primary pump is consisted of all pressure drop on the primary critical path. Any pressure drop on the secondary loop would only contribute to the calculated pressure drop of the secondary pump.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | One or more elements is not a pipe. -or- One or more elements is already the loop boundary. -or- One or more elements can not be used as loop boundary. Check if the element connects to any junction. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[PipingSystem Class](6abbdfa2-69a5-eef1-2663-89a5faf91831.htm)

[Autodesk.Revit.DB.Plumbing Namespace](cc553597-37c2-fcd9-6025-d904c129c80a.htm)