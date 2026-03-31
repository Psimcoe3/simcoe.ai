[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Item Property

---



|  |
| --- |
| [DimensionSegmentArray Class](ea274891-53e6-efbe-6dec-fc2c32636ad2.htm)   [See Also](#seeAlsoToggle) |

Gets or sets an item at a specified index within the array.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual DimensionSegment this[ 	int index ] { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Property Item ( _ 	index As Integer _ ) As DimensionSegment 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual property DimensionSegment^ Item[int index] { 	DimensionSegment^ get (int index); 	void set (int index, DimensionSegment^ value); } ``` |

#### Parameters

index
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The index of the item to be set or retrieved.

#### Return Value

Returns the object at the specified index.

# See Also

[DimensionSegmentArray Class](ea274891-53e6-efbe-6dec-fc2c32636ad2.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)