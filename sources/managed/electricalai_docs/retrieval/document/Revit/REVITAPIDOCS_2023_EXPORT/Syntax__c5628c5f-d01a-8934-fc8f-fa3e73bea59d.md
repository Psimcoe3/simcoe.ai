[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CanElementCutElement Method

---



|  |
| --- |
| [SolidSolidCutUtils Class](f1a2d176-2ab6-fa4c-293e-970c5866e87c.htm)   [See Also](#seeAlsoToggle) |

Verifies if the cutting element can add a solid cut to the target element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public static bool CanElementCutElement( 	Element cuttingElement, 	Element cutElement, 	out CutFailureReason reason ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CanElementCutElement ( _ 	cuttingElement As Element, _ 	cutElement As Element, _ 	<OutAttribute> ByRef reason As CutFailureReason _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool CanElementCutElement( 	Element^ cuttingElement,  	Element^ cutElement,  	[OutAttribute] CutFailureReason% reason ) ``` |

#### Parameters

cuttingElement
:   Type:  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
     The cutting element.

cutElement
:   Type:  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
     The element to be cut.

reason
:   Type:  [Autodesk.Revit.DB CutFailureReason](3ab731f0-b37a-49b9-0419-b5ca48df783d.htm)   %    
     The reason that the cutting element cannot add a solid cut to the cut element.

#### Return Value

True if the cutting element can add a solid cut to the target element, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[SolidSolidCutUtils Class](f1a2d176-2ab6-fa4c-293e-970c5866e87c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)