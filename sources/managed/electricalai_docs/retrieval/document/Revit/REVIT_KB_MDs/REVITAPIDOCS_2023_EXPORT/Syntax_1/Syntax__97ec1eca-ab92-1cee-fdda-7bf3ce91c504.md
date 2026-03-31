[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WriteJournalComment Method

---



|  |
| --- |
| [Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)   [See Also](#seeAlsoToggle) |

Writes a comment to the Revit journal file.

**Namespace:**   [Autodesk.Revit.ApplicationServices](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public void WriteJournalComment( 	string comment, 	bool timeStamp ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub WriteJournalComment ( _ 	comment As String, _ 	timeStamp As Boolean _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void WriteJournalComment( 	String^ comment,  	bool timeStamp ) ``` |

#### Parameters

comment
:   Type:  System String    
     Text for journal comment.

timeStamp
:   Type:  System Boolean    
     If a time stamp should be included in the journal comment.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)

[Autodesk.Revit.ApplicationServices Namespace](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)