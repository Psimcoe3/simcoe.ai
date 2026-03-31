[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetNumberingSequences Method

---



|  |
| --- |
| [NumberingSchema Class](8f2b22da-5963-301f-44d8-10c68828c436.htm)   [See Also](#seeAlsoToggle) |

Returns all numbering sequences within this numbering schema.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public IList<string> GetNumberingSequences() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetNumberingSequences As IList(Of String) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<String^>^ GetNumberingSequences() ``` |

#### Return Value

A collection of partition names of all numbering sequences currently present in this schema.

# Remarks

The collection may be empty if there are no elements yet in this schema.

One of the strings can be an empty string, which would indicate presence of the default partition into which elements automatically belong if left unassigned to any other partition

# See Also

[NumberingSchema Class](8f2b22da-5963-301f-44d8-10c68828c436.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)