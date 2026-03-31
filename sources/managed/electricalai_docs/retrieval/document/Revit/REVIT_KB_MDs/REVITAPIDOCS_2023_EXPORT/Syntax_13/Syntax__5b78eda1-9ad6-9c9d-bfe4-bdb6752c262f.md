[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetMinimumNumberOfDigits Method

---



|  |
| --- |
| [NumberingSchema Class](8f2b22da-5963-301f-44d8-10c68828c436.htm)   [See Also](#seeAlsoToggle) |

Sets a new value for the minimum number of digits to be used for formating the Number parameter of all numbered elements of the given document.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public static void SetMinimumNumberOfDigits( 	Document document, 	int value ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Sub SetMinimumNumberOfDigits ( _ 	document As Document, _ 	value As Integer _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: static void SetMinimumNumberOfDigits( 	Document^ document,  	int value ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document in which the new value will be in applied.

value
:   Type:  System Int32    
     New value for the minimum number of digits.

# Remarks

Valid values range from 1 to 10. Numbers with fewer digits than the minimum number will be padded with leading zeros.

The value affects all numbering schemas. Thus, once set, numbers for Rebar and Reinforcement Fabric will be formatted with the same minimum number of digits.

The current value can obtained by invoking the  [GetMinimumNumberOfDigits(Document)](80ac3f63-6383-ba62-380f-0e61b98e8dd7.htm)  method.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The minimum number of digits must be in range from 1 to 10. |
| [Autodesk.Revit.Exceptions ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document has no open transaction. |

# See Also

[NumberingSchema Class](8f2b22da-5963-301f-44d8-10c68828c436.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)