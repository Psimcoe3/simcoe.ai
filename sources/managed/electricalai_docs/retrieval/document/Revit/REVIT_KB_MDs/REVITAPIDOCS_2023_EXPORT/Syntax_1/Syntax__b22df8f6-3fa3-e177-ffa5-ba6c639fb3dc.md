[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CopyElements Method (Document, ICollection(ElementId), Document, Transform, CopyPasteOptions)

---



|  |
| --- |
| [ElementTransformUtils Class](82e737d5-fda4-bc10-6099-88999cd51300.htm)   [See Also](#seeAlsoToggle) |

Copies a set of elements from source document to destination document.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public static ICollection<ElementId> CopyElements( 	Document sourceDocument, 	ICollection<ElementId> elementsToCopy, 	Document destinationDocument, 	Transform transform, 	CopyPasteOptions options ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CopyElements ( _ 	sourceDocument As Document, _ 	elementsToCopy As ICollection(Of ElementId), _ 	destinationDocument As Document, _ 	transform As Transform, _ 	options As CopyPasteOptions _ ) As ICollection(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: static ICollection<ElementId^>^ CopyElements( 	Document^ sourceDocument,  	ICollection<ElementId^>^ elementsToCopy,  	Document^ destinationDocument,  	Transform^ transform,  	CopyPasteOptions^ options ) ``` |

#### Parameters

sourceDocument
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document that contains the elements to copy.

elementsToCopy
:   Type:  System.Collections.Generic ICollection   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The set of elements to copy.

destinationDocument
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The destination document to paste the elements into.

transform
:   Type:  [Autodesk.Revit.DB Transform](58dd01c8-b3fc-7142-e4f3-c524079a282d.htm)    
     The transform for the new elements. Can be    a null reference (  Nothing  in Visual Basic)  if no transform is required.

options
:   Type:  [Autodesk.Revit.DB CopyPasteOptions](d8f58fd5-2106-7a88-6218-106a30415791.htm)    
     Optional settings. Can be    a null reference (  Nothing  in Visual Basic)  if default settings should be used.

#### Return Value

The ids of the newly created copied elements.

# Remarks

Copies are placed at their respective original locations or locations specified by the optional transformation.

This method can be used for copying non-view specific elements only. For copying view-specific elements, use the view-specific form of the CopyElements method.

The destination document can be the same as the source document.

This method performs rehosting of elements where applicable.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given element id set is empty. -or- One or more elements in elementsToCopy do not exist in the document. -or- Some of the elements cannot be copied, because they are view-specific. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The elements cannot be copied. |
| [Autodesk.Revit.Exceptions OperationCanceledException](aea34480-ceb5-b49f-129d-0799e7bb1c21.htm) | User cancelled the operation. |

# See Also

[ElementTransformUtils Class](82e737d5-fda4-bc10-6099-88999cd51300.htm)

[CopyElements Overload](7b56b5c2-3aff-f42b-ab47-de1f89a1070f.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)