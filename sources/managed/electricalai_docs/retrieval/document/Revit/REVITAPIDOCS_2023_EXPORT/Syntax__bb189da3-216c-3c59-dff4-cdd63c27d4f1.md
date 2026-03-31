[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### JournalData Property

---



|  |
| --- |
| [ExternalCommandData Class](e9aab085-720f-b924-3ace-1f3c33d95d44.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

A data map that can be used to read and write data to the Autodesk Revit journal file.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public IDictionary<string, string> JournalData { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property JournalData As IDictionary(Of String, String) 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property IDictionary<String^, String^>^ JournalData { 	IDictionary<String^, String^>^ get (); 	void set (IDictionary<String^, String^>^ value); } ``` |

# Remarks

The data map is a string to string map that can be used to store data in the Revit journal file at the end of execution of the external command. If the command is then executed from the journal file during playback this data is then passed to the external command in this Data property so the external command can execute with this passed data in a UI-less mode, hence providing non interactive journal playback for automated testing purposes. For more information on Revit's journaling features contact the Autodesk Developer Network.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
void WriteJournalData(ExternalCommandData commandData)
{
    // Get the StringStringMap class which can write data into.
    IDictionary<String, String> dataMap = commandData.JournalData;
    dataMap.Clear();

    // Begin to add the support data
    dataMap.Add("Name", "Autodesk.Revit");
    dataMap.Add("Information", "This is an example.");
    dataMap.Add("Greeting", "Hello Everyone.");
}

/// <summary>
/// This sample shows how to get data from journal file. 
/// </summary>
void ReadJournalData(ExternalCommandData commandData)
{
    // Get the StringStringMap class which can write data into.
    IDictionary<String, String> dataMap = commandData.JournalData;

    // Begin to get the support data.
    String prompt = "Name: " + dataMap["Name"];
    prompt += "\nInformation: " + dataMap["Information"];
    prompt += "\nGreeting: " + dataMap["Greeting"];

    TaskDialog.Show("Revit",prompt);
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Sub WriteJournalData(commandData As ExternalCommandData)
    ' Get the StringStringMap class which can write data into.
    Dim dataMap As IDictionary(Of [String], [String]) = commandData.JournalData
    dataMap.Clear()

    ' Begin to add the support data
    dataMap.Add("Name", "Autodesk.Revit")
    dataMap.Add("Information", "This is an example.")
    dataMap.Add("Greeting", "Hello Everyone.")
End Sub

' <summary>
' This sample shows how to get data from journal file. 
' </summary>
Private Sub ReadJournalData(commandData As ExternalCommandData)
    ' Get the StringStringMap class which can write data into.
    Dim dataMap As IDictionary(Of [String], [String]) = commandData.JournalData

    ' Begin to get the support data.
    Dim prompt As [String] = "Name: " & dataMap("Name")
    prompt += vbLf & "Information: " & dataMap("Information")
    prompt += vbLf & "Greeting: " & dataMap("Greeting")

    TaskDialog.Show("Revit", prompt)
End Sub
```

# See Also

[ExternalCommandData Class](e9aab085-720f-b924-3ace-1f3c33d95d44.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)