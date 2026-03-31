[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MEPSystem Property

---



|  |
| --- |
| [MEPCurve Class](38714847-0f40-7021-aa79-2884c3a02ce2.htm)   [See Also](#seeAlsoToggle) |

The system of the MEP curve.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 19.0.0.0 (19.0.0.405)

# Syntax

| C# |
| --- |
| ``` public MEPSystem MEPSystem { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property MEPSystem As MEPSystem 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property MEPSystem^ MEPSystem { 	MEPSystem^ get (); } ``` |

# Remarks

Returns the system of this MEP curve. If the curve does not belong to any systems, the value will be    a null reference (  Nothing  in Visual Basic)  . If the curve belongs to more than one system, the first available value is returned.

# See Also

[MEPCurve Class](38714847-0f40-7021-aa79-2884c3a02ce2.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)