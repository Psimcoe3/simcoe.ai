[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetSectionByNumber Method

---



|  |
| --- |
| [MEPSystem Class](65946955-8638-fafb-2657-ef7cb7b2941b.htm)   [See Also](#seeAlsoToggle) |

Get the Section from section number

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public MEPSection GetSectionByNumber( 	int sectionNumber ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetSectionByNumber ( _ 	sectionNumber As Integer _ ) As MEPSection ``` |

 

| Visual C++ |
| --- |
| ``` public: MEPSection^ GetSectionByNumber( 	int sectionNumber ) ``` |

#### Parameters

sectionNumber
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The Section number.

#### Return Value

The section.    a null reference (  Nothing  in Visual Basic)  if the no section exists for the input section number.

# See Also

[MEPSystem Class](65946955-8638-fafb-2657-ef7cb7b2941b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)