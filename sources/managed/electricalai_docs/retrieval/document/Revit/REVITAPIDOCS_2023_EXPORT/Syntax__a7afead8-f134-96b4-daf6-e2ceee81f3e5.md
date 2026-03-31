[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetFaceReferences Method

---



|  |
| --- |
| [MassSurfaceData Class](69fcb13c-6443-d1c2-29d5-08adc1261afd.htm)   [See Also](#seeAlsoToggle) |

Gets References to the faces that the MassSurfaceData provides properties for.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public IList<Reference> GetFaceReferences() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetFaceReferences As IList(Of Reference) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<Reference^>^ GetFaceReferences() ``` |

#### Return Value

Returns an array of References to Faces that the MassSurfaceData provides properties for.

# Remarks

The results are always references to Faces. The Reference Type should be REFERENCE\_TYPE\_SURFACE. Currently Revit improperly reports it as REFERENCE\_TYPE\_NONE.

# See Also

[MassSurfaceData Class](69fcb13c-6443-d1c2-29d5-08adc1261afd.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)