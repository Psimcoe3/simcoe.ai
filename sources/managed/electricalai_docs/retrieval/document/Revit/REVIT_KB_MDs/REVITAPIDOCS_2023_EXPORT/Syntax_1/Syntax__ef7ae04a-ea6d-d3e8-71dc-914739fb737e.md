[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SequenceNumber Property

---



|  |
| --- |
| [Revision Class](af882c60-68ae-2e53-5c41-7aa43cfc1df4.htm)   [See Also](#seeAlsoToggle) |

The Sequence Number of this Revision.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public int SequenceNumber { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property SequenceNumber As Integer 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property int SequenceNumber { 	int get (); } ``` |

# Remarks

Every Revision in the project will be assigned a consecutive sequence number starting with 1. This number corresponds to the ordering of the Revisions. If a Revision is deleted, subsequent Revisions will update their sequence numbers to maintain a consecutive list.

# See Also

[Revision Class](af882c60-68ae-2e53-5c41-7aa43cfc1df4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)