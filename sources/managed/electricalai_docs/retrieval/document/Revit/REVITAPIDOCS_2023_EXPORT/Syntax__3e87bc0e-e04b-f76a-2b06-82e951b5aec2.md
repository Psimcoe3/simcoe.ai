[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExportPatternTable Class

---



|  |
| --- |
| [Members](e5b88354-d033-f559-f254-bbd7c84a72a1.htm)   [See Also](#seeAlsoToggle) |

A table supporting a mapping of FillPatterns in Revit to pattern names that will be set in the target export format.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public class ExportPatternTable : IEnumerable<KeyValuePair<ExportPatternKey, ExportPatternInfo>>,  	IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ExportPatternTable _ 	Implements IEnumerable(Of KeyValuePair(Of ExportPatternKey, ExportPatternInfo)),  _ 	IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ExportPatternTable : IEnumerable<KeyValuePair<ExportPatternKey^, ExportPatternInfo^>>,  	IDisposable ``` |

# Remarks

This table is structured as a mapping from  [ExportPatternKey](8e55a491-0886-37f5-b867-e4eea95276eb.htm)  to  [ExportPatternInfo](17621c1b-5f57-2a25-6ff9-73dfc67d5024.htm)  members. The  [ExportPatternKey](8e55a491-0886-37f5-b867-e4eea95276eb.htm)  contains the identification information for the pattern table: the Revit fill pattern type and name. The  [ExportPatternInfo](17621c1b-5f57-2a25-6ff9-73dfc67d5024.htm)  contains the pattern name to use in the export format.

The table can be accessed via direct iteration as a collection of KeyValuePairs, or by traversal of the stored keys obtained from GetKeys(), or via specific lookup of a key constructed externally. In all cases, the  [ExportPatternInfo](17621c1b-5f57-2a25-6ff9-73dfc67d5024.htm)  returned will be a copy of the  [ExportPatternInfo](17621c1b-5f57-2a25-6ff9-73dfc67d5024.htm)  from the table. In order to make changes to the  [ExportPatternInfo](17621c1b-5f57-2a25-6ff9-73dfc67d5024.htm)  and use those settings during export, set the modified  [ExportPatternInfo](17621c1b-5f57-2a25-6ff9-73dfc67d5024.htm)  back into the table using the same key.

# Inheritance Hierarchy

System Object    
  Autodesk.Revit.DB ExportPatternTable

# See Also

[ExportPatternTable Members](e5b88354-d033-f559-f254-bbd7c84a72a1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)