[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TextRange Constructor (Int32, Int32)

---



|  |
| --- |
| [TextRange Class](8a00baaf-8cb8-d9f0-e0a0-eaa5aa16e55e.htm)   [See Also](#seeAlsoToggle) |

Constructs a TextRange with input start and length.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public TextRange( 	int start, 	int length ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	start As Integer, _ 	length As Integer _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: TextRange( 	int start,  	int length ) ``` |

#### Parameters

start
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)

length
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)

# Remarks

The input value for start as well as length should not be negative.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The given value for start is negative. -or- The given value for length is negative. |

# See Also

[TextRange Class](8a00baaf-8cb8-d9f0-e0a0-eaa5aa16e55e.htm)

[TextRange Overload](417640e1-1c0f-6a90-cef4-3fe7cc037446.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)