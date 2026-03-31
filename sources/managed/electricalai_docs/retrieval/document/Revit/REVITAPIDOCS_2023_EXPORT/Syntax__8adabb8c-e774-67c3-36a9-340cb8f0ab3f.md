[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateCreasesFromFoldingLines Method

---



|  |
| --- |
| [SlabShapeEditor Class](06308ccc-46e7-6ff8-582c-6891af8b75e9.htm)   [See Also](#seeAlsoToggle) |

Convert selected folding lines to split lines

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public void CreateCreasesFromFoldingLines( 	Element hostObj, 	IList<Reference> references ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub CreateCreasesFromFoldingLines ( _ 	hostObj As Element, _ 	references As IList(Of Reference) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void CreateCreasesFromFoldingLines( 	Element^ hostObj,  	IList<Reference^>^ references ) ``` |

#### Parameters

hostObj
:   Type:  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
     object that hosts the SlabShapeEditor

references
:   Type:  System.Collections.Generic IList   [Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)    
     References of selected folding lines.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | this operation failed. |

# See Also

[SlabShapeEditor Class](06308ccc-46e7-6ff8-582c-6891af8b75e9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)