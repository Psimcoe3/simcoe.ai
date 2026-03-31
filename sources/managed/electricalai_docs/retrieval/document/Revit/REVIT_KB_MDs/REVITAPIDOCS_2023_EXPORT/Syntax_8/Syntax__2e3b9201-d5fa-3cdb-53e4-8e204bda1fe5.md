[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method

---



|  |
| --- |
| [AngularDimension Class](6f3b8d2e-904b-41cb-e57f-34fc8c1a0f4a.htm)   [See Also](#seeAlsoToggle) |

Creates a new instance of an Angular Dimension element within the project.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public static AngularDimension Create( 	Document document, 	View dbView, 	Arc arc, 	IList<Reference> references, 	DimensionType dimensionStyle ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	document As Document, _ 	dbView As View, _ 	arc As Arc, _ 	references As IList(Of Reference), _ 	dimensionStyle As DimensionType _ ) As AngularDimension ``` |

 

| Visual C++ |
| --- |
| ``` public: static AngularDimension^ Create( 	Document^ document,  	View^ dbView,  	Arc^ arc,  	IList<Reference^>^ references,  	DimensionType^ dimensionStyle ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document where new Angular Dimension is created.

dbView
:   Type:  [Autodesk.Revit.DB View](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)    
     The view in which the Angular Dimension will appear.

arc
:   Type:  [Autodesk.Revit.DB Arc](1f5f541e-9335-aef3-0e75-59eed9ae2221.htm)    
     Arc for the Angular Dimension.

references
:   Type:  System.Collections.Generic IList   [Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)    
     The references which the Angular Dimension will witness.

dimensionStyle
:   Type:  [Autodesk.Revit.DB DimensionType](a6f6655d-3383-a0ea-670d-0bbe6d2bb964.htm)    
     Dimension Style.

#### Return Value

The newly created Angular Dimension instance, or    a null reference (  Nothing  in Visual Basic)  if the operation fails.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | References should be: at least two, non parallel and rays of the arc passed. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document has no open transaction. |

# See Also

[AngularDimension Class](6f3b8d2e-904b-41cb-e57f-34fc8c1a0f4a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)