[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LogicalAndFilter Constructor (ElementFilter, ElementFilter)

---



|  |
| --- |
| [LogicalAndFilter Class](3e334aaf-2b39-58bd-d2cc-94e9c89bac57.htm)   [See Also](#seeAlsoToggle) |

Constructs a new instance of the logical filter with two input filters.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public LogicalAndFilter( 	ElementFilter filter1, 	ElementFilter filter2 ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	filter1 As ElementFilter, _ 	filter2 As ElementFilter _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: LogicalAndFilter( 	ElementFilter^ filter1,  	ElementFilter^ filter2 ) ``` |

#### Parameters

filter1
:   Type:  [Autodesk.Revit.DB ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)    
     The first filter.

filter2
:   Type:  [Autodesk.Revit.DB ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)    
     The second filter.

# Remarks

The input filters will be copied.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[LogicalAndFilter Class](3e334aaf-2b39-58bd-d2cc-94e9c89bac57.htm)

[LogicalAndFilter Overload](234a3298-2a67-ceae-cae0-c9b5f7a63680.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)