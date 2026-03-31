[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ChangeNumber Method

---



|  |
| --- |
| [NumberingSchema Class](8f2b22da-5963-301f-44d8-10c68828c436.htm)   [See Also](#seeAlsoToggle) |

Replaces an existing number with a new one (that does not exist yet).

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public IList<ElementId> ChangeNumber( 	string partition, 	int fromNumber, 	int toNumber ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function ChangeNumber ( _ 	partition As String, _ 	fromNumber As Integer, _ 	toNumber As Integer _ ) As IList(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<ElementId^>^ ChangeNumber( 	String^ partition,  	int fromNumber,  	int toNumber ) ``` |

#### Parameters

partition
:   Type:  System String    
     Name of the partition that identifies the sequence containing the number to be changed.

fromNumber
:   Type:  System Int32    
     Number to be changed; there must already be an element with that number in the sequence.

toNumber
:   Type:  System Int32    
     Number to change to; no element must have this number yet in the sequence.

#### Return Value

A collection of elements affected by the change of the number

# Remarks

This method gives the caller the ability to overwrite any number used in a given numbering sequence as long as the new number does not exist in the same sequence yet. If an attempt is made to replace a number by another that already exists, an exception will be thrown.

The new number will automatically be applied to all elements that bear the original number, thus those elements must be free to be modified. A collection of element Ids of all the affected elements is returned by this method.

The method is independent of the sequence's current starting number that might have been assigned previously, meaning that the new number will be accepted even if it is lower than the previously set start number in the sequence.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The sequence partition does not exist in the schema. -or- The specified sequence does not contain any elements with the given fromNumber. -or- There already are elements with the given toNumber in the specified sequence. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The value of toNumber must be in the range from 1 to the maximum value for an Integer type |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Either the schema or its document cannot be modified at present. |

# See Also

[NumberingSchema Class](8f2b22da-5963-301f-44d8-10c68828c436.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)