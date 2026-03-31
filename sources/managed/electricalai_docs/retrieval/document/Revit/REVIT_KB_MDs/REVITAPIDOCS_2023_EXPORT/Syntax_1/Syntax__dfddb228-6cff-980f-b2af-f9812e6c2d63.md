[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method

---



|  |
| --- |
| [ImageView Class](d81ffc17-044c-2671-c2f1-374e1dd90c53.htm)   [See Also](#seeAlsoToggle) |

Create an ImageView containing an image imported from disk.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2020

# Syntax

| C# |
| --- |
| ``` public static ImageView Create( 	Document document, 	ImageTypeOptions options ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	document As Document, _ 	options As ImageTypeOptions _ ) As ImageView ``` |

 

| Visual C++ |
| --- |
| ``` public: static ImageView^ Create( 	Document^ document,  	ImageTypeOptions^ options ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document in which to create the view.

options
:   Type:  [Autodesk.Revit.DB ImageTypeOptions](981135c3-777b-df9b-747f-60a35b74e00e.htm)    
     Options that specify what image to load.

#### Return Value

The newly created view.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | document is not a project document. -or- The image filename is an empty string. -or- The image file is not a supported image file type. -or- The image file is password protected. -or- The image file does not contain the requested page number. -or- The image file could not be read and may be corrupt. -or- An error occurred while handling the external resource corresponding to the image. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions FileArgumentNotFoundException](ca9ccaa9-ed08-d40d-31a7-1af3ad2dcb84.htm) | The image file does not exist. |
| [Autodesk.Revit.Exceptions ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document has no open transaction. |
| [Autodesk.Revit.Exceptions OptionalFunctionalityNotAvailableException](0612a676-b6ba-8c37-2e28-b197438305ab.htm) | The image file is a PDF file, but PDF import is not available in the installed Revit. |

# See Also

[ImageView Class](d81ffc17-044c-2671-c2f1-374e1dd90c53.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)