[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ReferencesDontMatchReferenceCategory Method

---



|  |
| --- |
| [MultiReferenceAnnotationOptions Class](2e081b6c-38fd-4f03-a372-0dfa841e6248.htm)   [See Also](#seeAlsoToggle) |

Verifies that all of the references belongs to elements which doesn't match the reference category required by the MultiReferenceAnnotationType.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2020

# Syntax

| C# |
| --- |
| ``` public bool ReferencesDontMatchReferenceCategory( 	IList<Reference> references ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function ReferencesDontMatchReferenceCategory ( _ 	references As IList(Of Reference) _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool ReferencesDontMatchReferenceCategory( 	IList<Reference^>^ references ) ``` |

#### Parameters

references
:   Type:  System.Collections.Generic IList   [Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)    
     The references to test.

#### Return Value

Returns true if the element categories of all tested references do not match the element category required by the MultiReferenceAnnotationType.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[MultiReferenceAnnotationOptions Class](2e081b6c-38fd-4f03-a372-0dfa841e6248.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)