[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Points Property

---



|  |
| --- |
| [FlexPipe Class](4b0e0656-4760-4a91-a777-ce50869a827a.htm)   [See Also](#seeAlsoToggle) |

The points of the flex pipe.

**Namespace:**   [Autodesk.Revit.DB.Plumbing](cc553597-37c2-fcd9-6025-d904c129c80a.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public IList<XYZ> Points { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Points As IList(Of XYZ) 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property IList<XYZ^>^ Points { 	IList<XYZ^>^ get (); 	void set (IList<XYZ^>^ value); } ``` |

# Remarks

This property is used to retrieve the points of flex pipe, including the end points. If the end points are changed, the connection will be maintained by Revit automatically. The set operation will fail if the modification makes the connection invalid.

# See Also

[FlexPipe Class](4b0e0656-4760-4a91-a777-ce50869a827a.htm)

[Autodesk.Revit.DB.Plumbing Namespace](cc553597-37c2-fcd9-6025-d904c129c80a.htm)