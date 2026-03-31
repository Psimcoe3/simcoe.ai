[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LeaderLeftAttachment Property

---



|  |
| --- |
| [TextNote Class](ecc1ce1c-d754-96d0-35db-ca2d1d84c57c.htm)   [See Also](#seeAlsoToggle) |

Attachment position of leaders on the left side of the text note.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public LeaderAtachement LeaderLeftAttachment { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property LeaderLeftAttachment As LeaderAtachement 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property LeaderAtachement LeaderLeftAttachment { 	LeaderAtachement get (); 	void set (LeaderAtachement value); } ``` |

# Remarks

The property controls the vertical position of leaders attached to the left side of the note.

Change of the value will affect all leaders currently attached to the left side.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[TextNote Class](ecc1ce1c-d754-96d0-35db-ca2d1d84c57c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)