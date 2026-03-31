[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CutExistsBetweenElements Method

---



|  |
| --- |
| [SolidSolidCutUtils Class](f1a2d176-2ab6-fa4c-293e-970c5866e87c.htm)   [See Also](#seeAlsoToggle) |

Checks that if there is a solid-solid cut between two elements.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public static bool CutExistsBetweenElements( 	Element first, 	Element second, 	out bool firstCutsSecond ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CutExistsBetweenElements ( _ 	first As Element, _ 	second As Element, _ 	<OutAttribute> ByRef firstCutsSecond As Boolean _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool CutExistsBetweenElements( 	Element^ first,  	Element^ second,  	[OutAttribute] bool% firstCutsSecond ) ``` |

#### Parameters

first
:   Type:  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
     The solid being cut or the cutting solid.

second
:   Type:  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
     The solid being cut or the cutting solid.

firstCutsSecond
:   Type:  System Boolean   %    
     If the return value of this function is true, this indicates which element is the cutting element from the pair. True if the first solid cuts the second one, false if the second solid cuts the first one.

#### Return Value

True if there is a solid-solid cut between the input elements, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[SolidSolidCutUtils Class](f1a2d176-2ab6-fa4c-293e-970c5866e87c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)