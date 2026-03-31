[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsOpen Method

---



|  |
| --- |
| [CurveLoop Class](84824924-cb89-9e20-de6e-3461f429dfd6.htm)   [See Also](#seeAlsoToggle) |

Returns whether the curve loop is open or closed, as determined by an internal flag.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public bool IsOpen() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsOpen As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsOpen() ``` |

#### Return Value

True if the CurveLoop is marked open, false if marked closed.

# Remarks

Some routines in Revit may set the CurveLoop to be marked "open" or "closed" in spite of the actual geometry of the curves. In these special cases, the CurveLoop class does not require that the CurveLoop is correctly marked.

# See Also

[CurveLoop Class](84824924-cb89-9e20-de6e-3461f429dfd6.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)