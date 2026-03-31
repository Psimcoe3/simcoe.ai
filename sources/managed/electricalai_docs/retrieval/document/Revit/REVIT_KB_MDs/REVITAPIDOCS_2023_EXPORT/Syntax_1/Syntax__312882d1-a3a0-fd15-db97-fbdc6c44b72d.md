[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetResultSchema Method

---



|  |
| --- |
| [SpatialFieldManager Class](0a6d155e-6ef1-7215-f8f1-c1d8203797ee.htm)   [See Also](#seeAlsoToggle) |

Sets a new value for an existing result schema in the result registry

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public void SetResultSchema( 	int idx, 	AnalysisResultSchema resultSchema ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetResultSchema ( _ 	idx As Integer, _ 	resultSchema As AnalysisResultSchema _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetResultSchema( 	int idx,  	AnalysisResultSchema^ resultSchema ) ``` |

#### Parameters

idx
:   Type:  System Int32    
     Index of registered result schema

resultSchema
:   Type:  [Autodesk.Revit.DB.Analysis AnalysisResultSchema](90969170-ac45-68e6-2527-f6fba5b3f7ae.htm)    
     Result schema replacing the existent one

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | idx refers to non-existent result schema -or- name of resultSchema is not unique in view |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[SpatialFieldManager Class](0a6d155e-6ef1-7215-f8f1-c1d8203797ee.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)