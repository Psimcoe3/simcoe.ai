[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LoadFamily Method (Document)

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [See Also](#seeAlsoToggle) |

Loads the contents of this family document into another document.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)

# Syntax

| C# |
| --- |
| ``` public Family LoadFamily( 	Document targetDocument ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function LoadFamily ( _ 	targetDocument As Document _ ) As Family ``` |

 

| Visual C++ |
| --- |
| ``` public: Family^ LoadFamily( 	Document^ targetDocument ) ``` |

#### Parameters

targetDocument
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The target document where the family will be loaded.

#### Return Value

Reference of the family in the target document.

# Remarks

If you are reloading an edited family back into the source document from which it was extracted, this method will always fail. This is because this method automatically suppresses the prompts Revit typically uses to deal with conflicts between families, and assumes that any such conflict should prevent the loading. If you want to be able to reload the same family into the source document, you should use the LoadFamily() overload accepting  [IFamilyLoadOptions](d447ed92-74e1-2125-dd0a-38a5ae85ce53.htm)  .

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the input argument-"targetDocument"-is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when the current document is not a family document, or when the target document is modifiable (e.g. there is an uncommitted transaction) or doesn't support load of this kind of families (e.g. loading a model family to detail family is disallowed), or when this family was found in the target document already and the conflict caused an automatic abort of the load operation, or when a shared family in this family was found in the target document already and the conflict caused an automatic abort of the load operation, or this document is currently in a read-only state. |
| [Autodesk.Revit.Exceptions ForbiddenForDynamicUpdateException](c5b911f6-1e8f-2cd4-6965-286f41221fe0.htm) | Thrown if this method is called during dynamic update. |

# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[LoadFamily Overload](2966229b-60b0-404d-5ffe-e4c4d85d2d7a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)