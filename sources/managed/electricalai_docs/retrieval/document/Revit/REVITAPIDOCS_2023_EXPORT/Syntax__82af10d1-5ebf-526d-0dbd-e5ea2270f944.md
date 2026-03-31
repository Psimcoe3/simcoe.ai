[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TransferredProjectStandards Event

---



|  |
| --- |
| [UIControlledApplication Class](4638c568-a118-1d57-ceed-a57595202644.htm)   [See Also](#seeAlsoToggle) |

Subscribe to the TransferredProjectStandards event to be notified after the scope of a Transfer Project Standards operation has been finalized.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2017.2

# Syntax

| C# |
| --- |
| ``` public event EventHandler<TransferredProjectStandardsEventArgs> TransferredProjectStandards ``` |

 

| Visual Basic |
| --- |
| ``` Public Event TransferredProjectStandards As EventHandler(Of TransferredProjectStandardsEventArgs) ``` |

 

| Visual C++ |
| --- |
| ``` public:  event EventHandler<TransferredProjectStandardsEventArgs^>^ TransferredProjectStandards { 	void add (EventHandler<TransferredProjectStandardsEventArgs^>^ value); 	void remove (EventHandler<TransferredProjectStandardsEventArgs^>^ value); } ``` |

# Remarks

This event is raised just after the native Revit items have been transferred, but before the transaction has been committed. An add-in that registered external items in  [TransferringProjectStandards](a7326050-7532-df52-a54a-8acd66a2a8a3.htm)  should subscribe to this event to carry out the transfer of any items that it registered if the user enabled those items for transfer. During the scope of this event, modification is permitted to the target document and modification is not permitted to the source document.

# See Also

[UIControlledApplication Class](4638c568-a118-1d57-ceed-a57595202644.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)