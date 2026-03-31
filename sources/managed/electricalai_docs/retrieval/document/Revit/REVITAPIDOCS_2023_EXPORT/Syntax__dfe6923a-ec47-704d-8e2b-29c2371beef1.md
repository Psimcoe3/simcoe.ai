[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DocumentReloadLatestProgressChangedEventArgs Class

---



|  |
| --- |
| [Members](fec6d68f-3b6f-837f-152a-193a16e6f58f.htm)   [See Also](#seeAlsoToggle) |

The event arguments used during the reload latest phase of  [!:Autodesk::Revit::ApplicationServices::Application::WorksharedOperationProgressChanged]  .

**Namespace:**   [Autodesk.Revit.DB.Events](b86712d6-83b3-e044-8016-f9881ecd3800.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2017 Subscription Update

# Syntax

| C# |
| --- |
| ``` public class DocumentReloadLatestProgressChangedEventArgs : DataTransferProgressChangedEventArgs ``` |

 

| Visual Basic |
| --- |
| ``` Public Class DocumentReloadLatestProgressChangedEventArgs _ 	Inherits DataTransferProgressChangedEventArgs ``` |

 

| Visual C++ |
| --- |
| ``` public ref class DocumentReloadLatestProgressChangedEventArgs : public DataTransferProgressChangedEventArgs ``` |

# Remarks

It is NOT recommended to do any time-consuming work when handling WorksharedOperationProgressChanged event. This can increase workshared operation time. Name correction - it is renamed from 'DocumentReloadLatestProgessChangedEventArgs' released since 2017 Subscription Update.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [System EventArgs](http://msdn2.microsoft.com/en-us/library/118wxtk3)    
  [Autodesk.Revit.DB.Events RevitAPIEventArgs](7c98499c-e345-cfda-ef89-48eccd3c9992.htm)    
  [Autodesk.Revit.DB.Events RevitAPISingleEventArgs](446fa3c6-4f35-47f4-e8c2-e5235c321836.htm)    
  [Autodesk.Revit.DB.Events WorksharedOperationProgressChangedEventArgs](110ee5e7-4cc1-3dbb-c824-6fd7bb5a8061.htm)    
  [Autodesk.Revit.DB.Events DataTransferProgressChangedEventArgs](a5a0081b-e990-ac8f-68dc-be0915955d1d.htm)    
  Autodesk.Revit.DB.Events DocumentReloadLatestProgressChangedEventArgs

# See Also

[DocumentReloadLatestProgressChangedEventArgs Members](fec6d68f-3b6f-837f-152a-193a16e6f58f.htm)

[Autodesk.Revit.DB.Events Namespace](b86712d6-83b3-e044-8016-f9881ecd3800.htm)