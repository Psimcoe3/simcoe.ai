[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateAnalysisDisplayStyle Method (Document, String, AnalysisDisplayDiagramSettings, AnalysisDisplayColorSettings, AnalysisDisplayLegendSettings)

---



|  |
| --- |
| [AnalysisDisplayStyle Class](927357e1-9874-8b73-72c8-ff2bb78bfa82.htm)   [See Also](#seeAlsoToggle) |

Factory method - creates analysis display style object of type Diagram for the given document.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static AnalysisDisplayStyle CreateAnalysisDisplayStyle( 	Document document, 	string name, 	AnalysisDisplayDiagramSettings diagramSettings, 	AnalysisDisplayColorSettings colorSettings, 	AnalysisDisplayLegendSettings legendSettings ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateAnalysisDisplayStyle ( _ 	document As Document, _ 	name As String, _ 	diagramSettings As AnalysisDisplayDiagramSettings, _ 	colorSettings As AnalysisDisplayColorSettings, _ 	legendSettings As AnalysisDisplayLegendSettings _ ) As AnalysisDisplayStyle ``` |

 

| Visual C++ |
| --- |
| ``` public: static AnalysisDisplayStyle^ CreateAnalysisDisplayStyle( 	Document^ document,  	String^ name,  	AnalysisDisplayDiagramSettings^ diagramSettings,  	AnalysisDisplayColorSettings^ colorSettings,  	AnalysisDisplayLegendSettings^ legendSettings ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     Document for which analysis display style object is created.

name
:   Type:  System String    
     Name of the analysis display style within the %document%.

diagramSettings
:   Type:  [Autodesk.Revit.DB.Analysis AnalysisDisplayDiagramSettings](57e0c5ff-555c-7345-ac24-3592207a4d70.htm)    
     Diagram settings for the style.

colorSettings
:   Type:  [Autodesk.Revit.DB.Analysis AnalysisDisplayColorSettings](936b709f-0cf4-c5ab-bfa9-2f4e340f4037.htm)    
     Color settings for the style.

legendSettings
:   Type:  [Autodesk.Revit.DB.Analysis AnalysisDisplayLegendSettings](a0362ecb-2442-6371-7e89-7a9ba66a0466.htm)    
     Legend settings for the style.

#### Return Value

New analysis display style object.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentsInconsistentException](05972c68-fa6d-3a83-d720-ad84fbc4780f.htm) | document is a family. -or- name is not unique in document. |

# See Also

[AnalysisDisplayStyle Class](927357e1-9874-8b73-72c8-ff2bb78bfa82.htm)

[CreateAnalysisDisplayStyle Overload](5b69a86f-b18e-e6d0-142a-2ed0343ccb89.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)