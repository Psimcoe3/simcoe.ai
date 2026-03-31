[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Item Property

---



|  |
| --- |
| [ReferenceArray Class](bc9192b5-6666-a8de-0128-87dae479fd6a.htm)   [See Also](#seeAlsoToggle) |

Gets or sets a reference at a specified index within the array.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual Reference this[ 	int index ] { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Property Item ( _ 	index As Integer _ ) As Reference 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual property Reference^ Item[int index] { 	Reference^ get (int index); 	void set (int index, Reference^ value); } ``` |

#### Parameters

index
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The index of the reference to be set or retrieved.

#### Return Value

Returns the reference at the specified index.

# See Also

[ReferenceArray Class](bc9192b5-6666-a8de-0128-87dae479fd6a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)