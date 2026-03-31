[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetAdditionalReferencesToDimension Method

---



|  |
| --- |
| [MultiReferenceAnnotationOptions Class](2e081b6c-38fd-4f03-a372-0dfa841e6248.htm)   [See Also](#seeAlsoToggle) |

Sets the additional references which the dimension will witness.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2020

# Syntax

| C# |
| --- |
| ``` public void SetAdditionalReferencesToDimension( 	IList<Reference> referencesToDimension ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetAdditionalReferencesToDimension ( _ 	referencesToDimension As IList(Of Reference) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetAdditionalReferencesToDimension( 	IList<Reference^>^ referencesToDimension ) ``` |

#### Parameters

referencesToDimension
:   Type:  System.Collections.Generic IList   [Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)    
     The additional references which the dimension will witness.

# Remarks

The additional references to dimension cannot come from the same category as the MultiReferenceAnnotationType's reference category.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Some references come from elements which directly match the reference category required by the MultiReferenceAnnotationType. For those elements please use SetElementsToDimension. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[MultiReferenceAnnotationOptions Class](2e081b6c-38fd-4f03-a372-0dfa841e6248.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)