[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsModifiable Property

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [See Also](#seeAlsoToggle) |

Identifies if the document is modifiable.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)

# Syntax

| C# |
| --- |
| ``` public bool IsModifiable { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property IsModifiable As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsModifiable { 	bool get (); } ``` |

# Remarks

This is not a permanent state such as, for example  [IsReadOnlyFile](c189f723-1465-0353-2ec1-57183905d73a.htm)  . Value of this property changes dynamically multiple times within the life-time of an open document. Regardless of the mode a document is opened with, the model can only be modified inside an open transaction. Furthermore, even with a transaction open, the model is not always modifiable. Though this is rather a rare situation, it can happen, most likely during model regeneration, failure processing, or some events. An attempt to modify a non-modifiable document will result in throwing a ModificationOutsideTransactionException. See also  [IsReadOnly](7e813a1b-9163-2509-f280-82572598432b.htm)

# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)