[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LoadFamily Method (Document, IFamilyLoadOptions)

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [See Also](#seeAlsoToggle) |

Loads the contents of this family document into another document.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public Family LoadFamily( 	Document targetDocument, 	IFamilyLoadOptions familyLoadOptions ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function LoadFamily ( _ 	targetDocument As Document, _ 	familyLoadOptions As IFamilyLoadOptions _ ) As Family ``` |

 

| Visual C++ |
| --- |
| ``` public: Family^ LoadFamily( 	Document^ targetDocument,  	IFamilyLoadOptions^ familyLoadOptions ) ``` |

#### Parameters

targetDocument
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The target document which the family will be loaded into.

familyLoadOptions
:   Type:  [Autodesk.Revit.DB IFamilyLoadOptions](d447ed92-74e1-2125-dd0a-38a5ae85ce53.htm)    
     The interface implementation to use when responding to conflicts during the load operation.

#### Return Value

Reference of the family in the target document.

# Remarks

If you are reloading an edited family back into the source document from which it was extracted, use this overload. This is because this overload allows you to respond to possible conflicts due to families already being present in the target document. The Revit API offers one automatic overload: RevitUIFamilyLoadOptions, which will show the same prompts to the user as seen during an interactive load.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the input argument-"targetDocument" or "familyLoadOptions"-is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when the current document is not a family document, or when the target document is modifiable (e.g. there is an uncommitted transaction) or doesn't support load of this kind of families (e.g. loading a model family to detail family is disallowed), or the load was cancelled due to a conflict and a False return from one of the interface methods, or this document is currently in a read-only state. |
| [Autodesk.Revit.Exceptions ForbiddenForDynamicUpdateException](c5b911f6-1e8f-2cd4-6965-286f41221fe0.htm) | Thrown if this method is called during dynamic update. |

# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[LoadFamily Overload](2966229b-60b0-404d-5ffe-e4c4d85d2d7a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)