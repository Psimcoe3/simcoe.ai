//
// (C) Copyright 2003-2025 by Autodesk, Inc.
//
// Permission to use, copy, modify, and distribute this software in
// object code form for any purpose and without fee is hereby granted,
// provided that the above copyright notice appears in all copies and
// that both that copyright notice and the limited warranty and
// restricted rights notice below appear in all supporting
// documentation.
//
// AUTODESK PROVIDES THIS PROGRAM "AS IS" AND WITH ALL FAULTS.
// AUTODESK SPECIFICALLY DISCLAIMS ANY IMPLIED WARRANTY OF
// MERCHANTABILITY OR FITNESS FOR A PARTICULAR USE. AUTODESK, INC.
// DOES NOT WARRANT THAT THE OPERATION OF THE PROGRAM WILL BE
// UNINTERRUPTED OR ERROR FREE.
//
// Use, duplication, or disclosure by the U.S. Government is subject to
// restrictions set forth in FAR 52.227-19 (Commercial Computer
// Software - Restricted Rights) and DFAR 252.227-7013(c)(1)(ii)
// (Rights in Technical Data and Computer Software), as applicable.
//

using Autodesk.Revit.DB.ExternalData;
using System.IO;
using System.Reflection;
using System.Text.Json;
using System.Text.Json.Serialization;

namespace Revit.SDK.Samples.CoordinationModel
{
   /// <summary>
   ///   These classes are used for reading/writing configuration settings for local and cloud files to be linked as coordination models
   /// </summary>
   class LocalFileCfg
   {
      public string FilePath { get; set; }
   }

   class LocalFileCurrentDirectoryCfg
   {
      public string FileName { get; set; }
   }
   class CloudFileCfg
   {
      public string AccountId { get; set; }
      public string ProjectId { get; set; }
      public string FileId { get; set; }
      public string ViewName { get; set; }
   }

   class CMConfig
   {
      public LocalFileCfg LocalFileCfg { get; set; }
      public LocalFileCurrentDirectoryCfg LocalFileCurrentDirectoryCfg { get; set; }
      public CloudFileCfg CloudFileCfg { get; set; }
      [JsonConverter(typeof(JsonStringEnumConverter))]
      public CoordinationModelPositioning Positioning { get; set; } = CoordinationModelPositioning.OriginToInternalOrigin;
   }

   class Config
   {
      static public CMConfig ReadConfig()
      {
         string currFolder = Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location);
         string settingsFileName = Path.Combine(currFolder, "CMSettings.json");
         string jsonString = File.ReadAllText(settingsFileName);
         CMConfig cmConfig = JsonSerializer.Deserialize<CMConfig>(jsonString);

         return cmConfig;
      }
   }
}