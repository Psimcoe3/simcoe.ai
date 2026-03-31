---
created: 2026-01-28T20:36:50 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Add-in Registration | Autodesk

> ## Excerpt
> External commands and external applications need to be registered in order to appear inside Revit. They can be registered by adding them to a .addin manifest file.

---
External commands and external applications need to be registered in order to appear inside Revit. They can be registered by adding them to a .addin manifest file.

The order that external commands and applications are listed in Revit is determined by the order in which they are read in when Revit starts up.

## Manifest Files

Revit API applications are registered with Revit via a .addin manifest file. Manifest files are read automatically by Revit when they are placed in one of two locations on a user's system:

In a non-user-specific location in "application data":

-   C:\\ProgramData\\Autodesk\\Revit\\Addins\\Revit 2018\\

In a user-specific location in "application data":

-   C:\\Users<user>\\AppData\\Roaming\\Autodesk\\Revit\\Addins\\Revit 2018\\

All files named .addin in these locations will be read and processed by Revit during startup. All of the files in both the user-specific location and the all users location are considered together and loaded in alphabetical order. If an all users manifest file shares the same name with a user-specific manifest file, the all users manifest file is ignored. Within each manifest file, the external commands and external applications are loaded in the order in which they are listed.

A basic file adding one ExternalCommand looks like this:

**Code Region 3-9: Manifest .addin ExternalCommand**

```
<?xml version="1.0" encoding="utf-8" standalone="no"?>
<RevitAddIns>
        <AddIn Type="Command">
                <Assembly>c:\MyProgram\MyProgram.dll</Assembly>
                <AddInId>76eb700a-2c85-4888-a78d-31429ecae9ed</AddInId>
                <FullClassName>Revit.Samples.SampleCommand</FullClassName>
                <Text>Sample command</Text>
                <VendorId>ADSK</VendorId>
                <VendorDescription>Autodesk, www.autodesk.com</VendorDescription> 
                <VisibilityMode>NotVisibleInFamily</VisibilityMode>
                <Discipline>Structure</Discipline>
                <Discipline>Architecture</Discipline>
                <AvailabilityClassName>Revit.Samples.SampleAccessibilityCheck</AvailabilityClassName>
                <LongDescription>
                        This is the long description for my command.
                        This is another descriptive paragraph, with notes about how to use the command properly.
                </LongDescription>
                <TooltipImage>c:\MyProgram\Autodesk.png</TooltipImage>
                <LargeImage>c:\MyProgram\MyProgramIcon.png</LargeImage>
        </AddIn>
</RevitAddIns>
```

A basic file adding one ExternalApplication looks like this:

**Code Region 3-10: Manifest .addin ExternalApplication**

```
<?xml version="1.0" encoding="utf-8" standalone="no"?>
<RevitAddIns>
<AddIn Type="Application">
                <Name>SampleApplication</Name>
                <Assembly>c:\MyProgram\MyProgram.dll</Assembly>
                <AddInId>604B1052-F742-4951-8576-C261D1993107</AddInId>
                <FullClassName>Revit.Samples.SampleApplication</FullClassName>
                <VendorId>ADSK</VendorId>
                <VendorDescription>Autodesk, www.autodesk.com</VendorDescription>
</AddIn>
</RevitAddIns>
```

A basic file adding one DB-level External Application looks like this:

**Code Region: Manifest .addin ExternalDBApplication**

```
<?xml version="1.0" encoding="utf-8" standalone="no"?>
<RevitAddIns>
<AddIn Type="DBApplication">
                <Assembly>c:\MyDBLevelApplication\MyDBLevelApplication.dll</Assembly>
                <AddInId>DA3D570A-1AB3-4a4b-B09F-8C15DFEC6BF0</AddInId>

                <FullClassName>MyCompany.MyDBLevelAddIn</FullClassName>

                <Name>My DB-Level AddIn</Name>                    
                <VendorId>ADSK</VendorId>
                <VendorDescription>Autodesk, www.autodesk.com</VendorDescription>
</AddIn>
</RevitAddIns>
```

Multiple AddIn elements may be provided in a single manifest file.

The following table describes the available XML tags:

<table summary="" id="GUID-4FFDB03E-6936-417C-9772-8FC258A261F7__TABLE_8E7A8ACAD3C5487CA4A1E985DF05CA47"><tbody><tr><td><b>Tag</b></td><td><b>Description</b></td></tr><tr><td>Assembly</td><td>The full path to the add-in assembly file. Required for all ExternalCommands and ExternalApplications.</td></tr><tr><td>FullClassName</td><td>The full name of the class in the assembly file which implements IExternalCommand or IExternalApplication. Required for all ExternalCommands and ExternalApplications.</td></tr><tr><td>AddInId</td><td>A GUID which represents the id of this particular application. AddInIds must be unique for a given session of Revit.<p>Autodesk recommends you generate a unique GUID for each registered application or command. Required for all ExternalCommands and ExternalApplications.</p></td></tr><tr><td>Name</td><td>The name of application. Required; for ExternalApplications only.</td></tr><tr><td>Text</td><td>The name of the button. Optional; use this tag for ExternalCommands only. The default is "External Tool".</td></tr><tr><td>VendorId</td><td>A unique vendor identifier that may be used by some operations in Revit (such as identification of extensible storage). This must be unique, and thus we recommend to use reversed version of your domain name, for example, com.autodesk or uk.co.autodesk.</td></tr><tr><td>VendorDescription</td><td>Description containing vendor's legal name and/or other pertinent information. Optional.</td></tr><tr><td>Description</td><td>Short description of the command, will be used as the button tooltip. Optional; use this tag for ExternalCommands only.<p>The default is a tooltip with just the command text.</p></td></tr><tr><td>VisibilityMode</td><td>The modes in which the external command will be visible. Multiple values may be set for this option. Optional; use this tag for ExternalCommands only.<p>The default is to display the command in all modes, including when there is no active document. Previously written external commands which need to run against the active document should either be modified to ensure that the code deals with invocation of the command when there is no active document, or apply the NotVisibleWhenNoActiveDocument mode. See table below for more information.</p></td></tr><tr><td>Discipline</td><td>The disciplines in which the external command will be visible. Multiple values may be set for this option. Optional; use this tag for ExternalCommands only.<p>The default is to display the command in all disciplines. If any specific disciplines are listed, the command will only be visible in those disciplines. See table below for more information.</p></td></tr><tr><td>AvailabilityClassName</td><td>The full name of the class in the assembly file which implemented IExternalCommandAvailability. This class allows the command button to be selectively grayed out depending on context. Optional; use this tag for ExternalCommands only.<p>The default is a command that is available whenever it is visible.</p></td></tr><tr><td>LargeImage</td><td>The icon to use for the button in the External Tools pulldown menu. Optional; use this tag for ExternalCommands only.<p>The default is to show a button without an icon.</p></td></tr><tr><td>SmallImage</td><td>The icon to use if the button is promoted to the Quick Access Toolbar. Optional; use this tag for ExternalCommands only.<p>The default is to show a Quick Access Toolbar button without an icon, which can be confusing to users.</p></td></tr><tr><td>LongDescription</td><td>Long description of the command, will be used as part of the button extended tooltip, shown when the mouse hovers over the command for a longer amount of time. Optional; use this tag for ExternalCommands only. If this property and TooltipImage are not supplied, the button will not have an extended tooltip.</td></tr><tr><td>TooltipImage</td><td>An image file to show as a part of the button extended tooltip, shown when the mouse hovers over the command for a longer amount of time. Optional; use this tag for ExternalCommands only. If this property and TooltipImage are not supplied, the button will not have an extended tooltip.</td></tr><tr><td>LanguageType</td><td>Localization setting for Text, Description, LargeImage, LongDescription, and TooltipImage of external tools buttons. Revit will load the resource values from the specified language resource dll. The value can be one of the eleven languages supported by Revit. If no LanguageType is specified, the language resource which the current session of Revit is using will be automatically loaded. For more details see the section on Localization.</td></tr><tr><td>AllowLoadIntoExistingSession</td><td>The flag for loading permission. Set to false to prevent Revit from automatically loading addins in a newly added .addin manifest file without restarting. Optional. By default. Revit will automatically load addins from newly added .addin manifest files without restarting Revit.</td></tr></tbody></table>

\*\*Table 3: VisibilityMode Members\*\*

<table summary="" id="GUID-4FFDB03E-6936-417C-9772-8FC258A261F7__TABLE_531B8743F3B5484A9E1F35FEA9630769"><tbody><tr><td><b>Member Name</b></td><td><b>Description</b></td></tr><tr><td>AlwaysVisible</td><td>The command is available in all possible modes supported by the Revit API.</td></tr><tr><td>NotVisibleInProject</td><td>The command is invisible when there is a project document active.</td></tr><tr><td>NotVisibleInFamily</td><td>The command is invisible when there is a family document active.</td></tr><tr><td>NotVisibleWhenNoActiveDocument</td><td>The command is invisible when there is no active document.</td></tr></tbody></table>

\*\*Table 4: Discipline Members\*\*

<table summary="" id="GUID-4FFDB03E-6936-417C-9772-8FC258A261F7__TABLE_D0B11ECA4EE848D58871A442BD3B4A5C"><tbody><tr><td><b>Member Name</b></td><td><b>Description</b></td></tr><tr><td>Any</td><td>The command is available in all possible disciplines supported by the Revit API.</td></tr><tr><td>Architecture</td><td>The command is visible in Autodesk Revit Architecture.</td></tr><tr><td>Structure</td><td>The command is visible in Autodesk Revit Structure.</td></tr><tr><td>StructuralAnalysis</td><td>The command is visible when the Structural Analysis discipline editing tools are available.</td></tr><tr><td>MassingAndSite</td><td>The command is visible when the Massing and Site discipline editing tools are available.</td></tr><tr><td>EnergyAnalysis</td><td>The command is visible when Energy Analysis discipline editing tools are available.</td></tr><tr><td>Mechanical</td><td>The command is visible when the Mechanical discipline editing tools are available, e.g. in Autodesk Revit MEP.</td></tr><tr><td>Electrical</td><td>The command is visible when the Electrical discipline editing tools are available, e.g. in Autodesk Revit MEP.</td></tr><tr><td>Piping</td><td>The command is visible when the Piping discipline editing tools are available, e.g. in Autodesk Revit MEP.</td></tr><tr><td>MechanicalAnalysis</td><td>The command is visible when the Mechanical Analysis discipline editing tools are available.</td></tr><tr><td>PipingAnalysis</td><td>The command is visible when the Piping Analysis discipline editing tools are available.</td></tr><tr><td>ElectricalAnalysis</td><td>The command is visible when the Electrical Analysis discipline editing tools are available.</td></tr></tbody></table>

## .NET Add-in Utility for manifest files

The .NET utility DLL RevitAddInUtility.dll offers a dedicated API capable of reading, writing and modifying Revit Add-In manifest files. It is intended for use from product installers and scripts. Consult the API documentation in the RevitAddInUtility.chm help file in the SDK installation folder.

<table summary="" id="GUID-4FFDB03E-6936-417C-9772-8FC258A261F7__TABLE_796DAC6A9FB94CC8958CB909E81D9355"><tbody><tr><td><b>Code Region 3-11: Creating and editing a manifest file</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>ManifestFile</span><span>()</span><span>
</span><span>{</span><span>
        </span><span>//create a new addin manifest</span><span>
        </span><span>RevitAddInManifest</span><span> </span><span>Manifest</span><span> </span><span>=</span><span> </span><span>new</span><span> </span><span>RevitAddInManifest</span><span>();</span><span>

        </span><span>//create an external command</span><span>
        </span><span>RevitAddInCommand</span><span> command1 </span><span>=</span><span> </span><span>new</span><span> </span><span>RevitAddInCommand</span><span>(</span><span>"full path\\assemblyName.dll"</span><span>,</span><span> 
        </span><span>Guid</span><span>.</span><span>NewGuid</span><span>(),</span><span> </span><span>"namespace.className"</span><span>,</span><span> </span><span>"ADSK"</span><span>);</span><span>
        command1</span><span>.</span><span>Description</span><span> </span><span>=</span><span> </span><span>"description"</span><span>;</span><span>
        command1</span><span>.</span><span>Text</span><span> </span><span>=</span><span> </span><span>"display text"</span><span>;</span><span>

        </span><span>// this command only visible in Revit MEP, Structure, and only visible </span><span>
        </span><span>// in Project document or when no document at all</span><span>
        command1</span><span>.</span><span>Discipline</span><span> </span><span>=</span><span> </span><span>Discipline</span><span>.</span><span>Mechanical</span><span> </span><span>|</span><span> </span><span>Discipline</span><span>.</span><span>Electrical</span><span> </span><span>|</span><span>
                                </span><span>Discipline</span><span>.</span><span>Piping</span><span> </span><span>|</span><span> </span><span>Discipline</span><span>.</span><span>Structure</span><span>;</span><span>
        command1</span><span>.</span><span>VisibilityMode</span><span> </span><span>=</span><span> </span><span>VisibilityMode</span><span>.</span><span>NotVisibleInFamily</span><span>;</span><span>

        </span><span>//create an external application</span><span>
        </span><span>RevitAddInApplication</span><span> application1 </span><span>=</span><span> </span><span>new</span><span> </span><span>RevitAddInApplication</span><span>(</span><span>"appName"</span><span>,</span><span>
        </span><span>"full path\\assemblyName.dll"</span><span>,</span><span> </span><span>Guid</span><span>.</span><span>NewGuid</span><span>(),</span><span> </span><span>"namespace.className"</span><span>,</span><span> </span><span>"ADSK"</span><span>);</span><span>

        </span><span>//add both command(s) and application(s) into manifest</span><span>
        </span><span>Manifest</span><span>.</span><span>AddInCommands</span><span>.</span><span>Add</span><span>(</span><span>command1</span><span>);</span><span>
        </span><span>Manifest</span><span>.</span><span>AddInApplications</span><span>.</span><span>Add</span><span>(</span><span>application1</span><span>);</span><span>

        </span><span>//save manifest to a file</span><span>
        </span><span>RevitProduct</span><span> revitProduct1 </span><span>=</span><span> </span><span>RevitProductUtility</span><span>.</span><span>GetAllInstalledRevitProducts</span><span>()[</span><span>0</span><span>];</span><span>
        </span><span>Manifest</span><span>.</span><span>SaveAs</span><span>(</span><span>revitProduct1</span><span>.</span><span>AllUsersAddInFolder</span><span> </span><span>+</span><span> </span><span>"\\RevitAddInUtilitySample.addin"</span><span>);</span><span>
        </span><span>}</span></code></pre></td></tr></tbody></table>

<table summary="" id="GUID-4FFDB03E-6936-417C-9772-8FC258A261F7__TABLE_A7DA7C3527FB43B8AF8CCF19FAAAB290"><tbody><tr><td><b>Code Region 3-12: Reading an existing manifest file</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>ReadManifest</span><span>()</span><span>
</span><span>{</span><span>
        </span><span>RevitProduct</span><span> revitProduct1 </span><span>=</span><span> </span><span>RevitProductUtility</span><span>.</span><span>GetAllInstalledRevitProducts</span><span>()[</span><span>0</span><span>];</span><span>

        </span><span>RevitAddInManifest</span><span> revitAddInManifest </span><span>=</span><span> 
     </span><span>Autodesk</span><span>.</span><span>RevitAddIns</span><span>.</span><span>AddInManifestUtility</span><span>.</span><span>GetRevitAddInManifest</span><span>(</span><span>
          revitProduct1</span><span>.</span><span>AllUsersAddInFolder</span><span> </span><span>+</span><span> </span><span>"\\RevitAddInUtilitySample.addin"</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

## Access to add-in data paths

Autodesk.Revit.ApplicationServices.Application.CurrentUsersAddinsDataFolderPath provides access to add-in data folder for the current Revit version and current user (such as %appdata%\\Autodesk\\Revit\\Autodesk Revit 2019\\AddinsData)
