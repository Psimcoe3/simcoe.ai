[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AreElementsValidForMultiReferenceAnnotation Method

---



|  |
| --- |
| [MultiReferenceAnnotation Class](2224ac33-d7c0-bda8-70de-0005023c2149.htm)   [See Also](#seeAlsoToggle) |

The method validates if the input elements match the element category id for the MultiReferenceAnnotationType.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2020

# Syntax

| C# |
| --- |
| ``` public static bool AreElementsValidForMultiReferenceAnnotation( 	Document document, 	MultiReferenceAnnotationOptions options ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function AreElementsValidForMultiReferenceAnnotation ( _ 	document As Document, _ 	options As MultiReferenceAnnotationOptions _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool AreElementsValidForMultiReferenceAnnotation( 	Document^ document,  	MultiReferenceAnnotationOptions^ options ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document for the multi-reference annotation.

options
:   Type:  [Autodesk.Revit.DB MultiReferenceAnnotationOptions](2e081b6c-38fd-4f03-a372-0dfa841e6248.htm)    
     The creation options for the new MultiReferenceAnnotation.

#### Return Value

Returns true if the input elements match the element category id for the MultiReferenceAnnotationType, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[MultiReferenceAnnotation Class](2224ac33-d7c0-bda8-70de-0005023c2149.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)