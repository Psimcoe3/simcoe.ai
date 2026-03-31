[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WorksharedOperationProgressChangedEventArgs Class

---



|  |
| --- |
| [Members](4bf59c13-b078-123b-aaab-e0d547160675.htm)   [See Also](#seeAlsoToggle) |

The event arguments used by the WorksharedOperationProgressChanged event, this event will be raised when executing following workshared operations.

**Namespace:**   [Autodesk.Revit.DB.Events](b86712d6-83b3-e044-8016-f9881ecd3800.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2017 Subscription Update

# Syntax

| C# |
| --- |
| ``` public class WorksharedOperationProgressChangedEventArgs : RevitAPISingleEventArgs ``` |

 

| Visual Basic |
| --- |
| ``` Public Class WorksharedOperationProgressChangedEventArgs _ 	Inherits RevitAPISingleEventArgs ``` |

 

| Visual C++ |
| --- |
| ``` public ref class WorksharedOperationProgressChangedEventArgs : public RevitAPISingleEventArgs ``` |

# Remarks

# Remarks

For synchronizing with central operation, there are 4 steps. 1) Save to local (before save to central) - Serializes the streams from memory to local disk cache;  [!:Autodesk::Revit::DB::Events::DocumentSaveToLocalProgressChangedEventArgs]  2) Reload latest - Downloads the streams from central model on server and merge them into local memory;  [!:Autodesk::Revit::DB::Events::DocumentReloadLatestProgressChangedEventArgs]  3) Save to central - Uploads merged streams from local memory to server central model;  [!:Autodesk::Revit::DB::Events::DocumentSaveToCentralProgressChangedEventArgs]  4) Save to local (after save to central) - Serializes the merged streams from memory to local disk cache;  [!:Autodesk::Revit::DB::Events::DocumentSaveToLocalProgressChangedEventArgs]

For document open operation, just download the model from server and then open it;  [!:Autodesk::Revit::DB::Events::CreateRelatedFileProgressChangedEventArgs]

It is NOT recommended to deal with time-consuming work when handling WorksharedOperationProgressChanged event, otherwise it would increase synchronizing with central or model open time.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [System EventArgs](http://msdn2.microsoft.com/en-us/library/118wxtk3)    
  [Autodesk.Revit.DB.Events RevitAPIEventArgs](7c98499c-e345-cfda-ef89-48eccd3c9992.htm)    
  [Autodesk.Revit.DB.Events RevitAPISingleEventArgs](446fa3c6-4f35-47f4-e8c2-e5235c321836.htm)    
  Autodesk.Revit.DB.Events WorksharedOperationProgressChangedEventArgs    
  [Autodesk.Revit.DB.Events DataTransferProgressChangedEventArgs](a5a0081b-e990-ac8f-68dc-be0915955d1d.htm)    
  [Autodesk.Revit.DB.Events DocumentSaveToLocalProgressChangedEventArgs](a3a774b8-2913-5de6-e7ad-5daa24a9c172.htm)

# See Also

[WorksharedOperationProgressChangedEventArgs Members](4bf59c13-b078-123b-aaab-e0d547160675.htm)

[Autodesk.Revit.DB.Events Namespace](b86712d6-83b3-e044-8016-f9881ecd3800.htm)