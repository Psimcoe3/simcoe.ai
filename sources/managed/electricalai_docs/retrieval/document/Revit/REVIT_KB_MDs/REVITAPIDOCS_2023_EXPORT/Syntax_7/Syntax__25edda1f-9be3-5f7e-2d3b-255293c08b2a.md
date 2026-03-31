[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateDefault Method

---



|  |
| --- |
| [MultiReferenceAnnotationType Class](046b4d91-40b3-4dd0-be1b-635fb30956c2.htm)   [See Also](#seeAlsoToggle) |

Creates the first MultiReferenceAnnotationType element and adds it to the document.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public static MultiReferenceAnnotationType CreateDefault( 	Document document ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateDefault ( _ 	document As Document _ ) As MultiReferenceAnnotationType ``` |

 

| Visual C++ |
| --- |
| ``` public: static MultiReferenceAnnotationType^ CreateDefault( 	Document^ document ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document to be modified.

#### Return Value

The new MultiReferenceAnnotationType element.

# Remarks

If there is no existing MultiReferenceAnnotationType a new one will be created, otherwise an exception will be thrown. Use  [Duplicate(String)](b0e7d5d5-f33a-8ff2-b471-78a213f06ef5.htm)  to create all further MultiReferenceAnnotationTypes. The default MultiReferenceAnnotationType will use the document's current default linear dimension style and will have Structural Rebar as its reference category. No tag type will be set for the new MultiReferenceAnnotationType.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | document is not a project document. -or- There are existing MultiReferenceAnnotationTypes in the document. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[MultiReferenceAnnotationType Class](046b4d91-40b3-4dd0-be1b-635fb30956c2.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)