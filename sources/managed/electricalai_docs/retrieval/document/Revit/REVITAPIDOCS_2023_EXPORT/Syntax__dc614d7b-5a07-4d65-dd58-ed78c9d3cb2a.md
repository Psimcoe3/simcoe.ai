[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RemoveCutBetweenSolids Method

---



|  |
| --- |
| [SolidSolidCutUtils Class](f1a2d176-2ab6-fa4c-293e-970c5866e87c.htm)   [See Also](#seeAlsoToggle) |

Removes the solid-solid cut between the two elements if it exists.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public static void RemoveCutBetweenSolids( 	Document document, 	Element first, 	Element second ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Sub RemoveCutBetweenSolids ( _ 	document As Document, _ 	first As Element, _ 	second As Element _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: static void RemoveCutBetweenSolids( 	Document^ document,  	Element^ first,  	Element^ second ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document containing the two elements

first
:   Type:  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
     The solid being cut or the cutting solid.

second
:   Type:  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
     The solid being cut or the cutting solid.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[SolidSolidCutUtils Class](f1a2d176-2ab6-fa4c-293e-970c5866e87c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)