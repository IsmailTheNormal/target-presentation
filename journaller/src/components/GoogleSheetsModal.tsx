import React, { useState, useEffect } from 'react';
import { 
  X, 
  FileSpreadsheet, 
  Copy, 
  Check, 
  Download, 
  Code2, 
  CheckCircle2,
  AlertTriangle,
  Radio,
  RefreshCw,
  Zap,
  ExternalLink,
  ShieldCheck,
  Layers,
  ArrowRight
} from 'lucide-react';
import { ClassData } from '../types/gradebook';
import { generateGoogleAppsScript } from '../utils/googleSheetsIntegration';
import { 
  getSavedWebhookUrl, 
  saveWebhookUrl, 
  getAutoSyncEnabled, 
  setAutoSyncEnabled, 
  testWebhookConnection, 
  syncClassToGoogleSheets,
  SyncStatus
} from '../utils/googleSheetsSync';

interface GoogleSheetsModalProps {
  classData: ClassData;
  onClose: () => void;
  onSyncSuccess?: (time: Date) => void;
}

export const GoogleSheetsModal: React.FC<GoogleSheetsModalProps> = ({
  classData,
  onClose,
  onSyncSuccess,
}) => {
  const [activeTab, setActiveTab] = useState<'autosync' | 'script' | 'excel'>('autosync');
  const [webhookUrl, setWebhookUrl] = useState(getSavedWebhookUrl());
  const [autoSyncEnabled, setAutoSync] = useState(getAutoSyncEnabled());
  const [testing, setTesting] = useState(false);
  const [manualSyncing, setManualSyncing] = useState(false);
  const [testResult, setTestResult] = useState<{ success: boolean; message: string; sheetTitle?: string } | null>(null);
  const [copiedCode, setCopiedCode] = useState(false);

  const appsScriptCode = generateGoogleAppsScript(classData);

  const handleTestConnection = async () => {
    if (!webhookUrl.trim()) return;
    setTesting(true);
    setTestResult(null);

    const res = await testWebhookConnection(webhookUrl.trim());
    setTesting(false);
    setTestResult(res);

    if (res.success) {
      saveWebhookUrl(webhookUrl.trim());
    }
  };

  const handleSaveAndSyncNow = async () => {
    saveWebhookUrl(webhookUrl.trim());
    setAutoSyncEnabled(autoSyncEnabled);

    setManualSyncing(true);
    const res = await syncClassToGoogleSheets(classData, webhookUrl.trim());
    setManualSyncing(false);

    if (res.success) {
      setTestResult({ success: true, message: 'Google Sheet updated with all current student marks!' });
      if (onSyncSuccess) onSyncSuccess(res.timestamp);
    } else {
      setTestResult({ success: false, message: res.message });
    }
  };

  const handleCopyCode = () => {
    navigator.clipboard.writeText(appsScriptCode);
    setCopiedCode(true);
    setTimeout(() => setCopiedCode(false), 2500);
  };

  const handleDownloadExcel = () => {
    const link = document.createElement('a');
    link.href = '/Teacher_Production_Gradebook.xlsx';
    link.download = 'Teacher_Production_Gradebook.xlsx';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-sm overflow-y-auto">
      <div className="bg-white rounded-3xl shadow-2xl border border-slate-200 w-full max-w-3xl my-8 overflow-hidden transition-all">
        
        {/* Header */}
        <div className="px-6 py-4 border-b border-slate-200 bg-gradient-to-r from-emerald-800 to-teal-900 text-white flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-2xl bg-white/10 flex items-center justify-center shadow-inner">
              <FileSpreadsheet className="w-6 h-6 text-white" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <h2 className="text-lg font-extrabold">Continuous Google Sheets Sync</h2>
                <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-400 text-emerald-950">
                  Real-Time
                </span>
              </div>
              <p className="text-xs text-emerald-200">
                Saves and updates marks in your Google Sheet continuously on every edit
              </p>
            </div>
          </div>

          <button
            onClick={onClose}
            className="p-1.5 hover:bg-white/20 rounded-xl text-emerald-200 hover:text-white transition"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Navigation Tabs */}
        <div className="flex border-b border-slate-200 bg-slate-50 px-6 pt-3 gap-2 overflow-x-auto">
          <button
            onClick={() => setActiveTab('autosync')}
            className={`px-4 py-2.5 text-xs font-bold border-b-2 transition flex items-center gap-2 whitespace-nowrap ${
              activeTab === 'autosync'
                ? 'border-emerald-600 text-emerald-800 bg-white rounded-t-xl shadow-sm'
                : 'border-transparent text-slate-600 hover:text-slate-900'
            }`}
          >
            <Zap className="w-4 h-4 text-emerald-600" />
            <span>⚡ Real-Time Auto-Save Setup</span>
          </button>

          <button
            onClick={() => setActiveTab('script')}
            className={`px-4 py-2.5 text-xs font-bold border-b-2 transition flex items-center gap-2 whitespace-nowrap ${
              activeTab === 'script'
                ? 'border-emerald-600 text-emerald-800 bg-white rounded-t-xl shadow-sm'
                : 'border-transparent text-slate-600 hover:text-slate-900'
            }`}
          >
            <Code2 className="w-4 h-4" />
            <span>Google Apps Script (Code.gs)</span>
          </button>

          <button
            onClick={() => setActiveTab('excel')}
            className={`px-4 py-2.5 text-xs font-bold border-b-2 transition flex items-center gap-2 whitespace-nowrap ${
              activeTab === 'excel'
                ? 'border-emerald-600 text-emerald-800 bg-white rounded-t-xl shadow-sm'
                : 'border-transparent text-slate-600 hover:text-slate-900'
            }`}
          >
            <Download className="w-4 h-4" />
            <span>Offline Workbook (.xlsx)</span>
          </button>
        </div>

        {/* Modal Content */}
        <div className="p-6">
          
          {/* TAB 1: Real-Time Auto-Save Setup */}
          {activeTab === 'autosync' && (
            <div className="space-y-5">
              
              {/* Feature highlight */}
              <div className="bg-emerald-50 border border-emerald-200 rounded-2xl p-4 flex items-start gap-3">
                <div className="w-8 h-8 rounded-xl bg-emerald-100 flex items-center justify-center shrink-0 text-emerald-700 font-bold">
                  ⚡
                </div>
                <div className="text-xs text-emerald-950">
                  <p className="font-bold text-sm text-emerald-900 mb-0.5">
                    Continuous 2-Way Save & Update
                  </p>
                  <p className="text-emerald-800 leading-relaxed">
                    Once connected, you do NOT need to copy-paste. Every grade you type, student you add, or category you adjust is <strong>automatically saved and updated to your Google Sheet in real-time</strong>.
                  </p>
                </div>
              </div>

              {/* Step-by-step instructions */}
              <div className="border border-slate-200 rounded-2xl p-4 bg-slate-50 space-y-3">
                <span className="text-xs font-bold text-slate-700 uppercase tracking-wider block">
                  Quick 1-Minute Connection Steps
                </span>
                
                <ol className="list-decimal list-inside text-xs text-slate-700 space-y-1.5 font-medium">
                  <li>In your Google Sheet, open <strong>Extensions &gt; Apps Script</strong>.</li>
                  <li>Paste the code from the <strong>"Google Apps Script"</strong> tab into the editor and click <strong>Save</strong>.</li>
                  <li>Click <strong>Deploy &gt; New deployment &gt; Select "Web app"</strong>.</li>
                  <li>Set <em>"Who has access"</em> to <strong>"Anyone"</strong>, click <strong>Deploy</strong>, and copy your Web App URL.</li>
                  <li>Paste your Web App URL below and click <strong>"Connect & Sync Now"</strong>!</li>
                </ol>
              </div>

              {/* Web App URL Input */}
              <div className="space-y-2">
                <label className="block text-xs font-bold text-slate-700 uppercase tracking-wider">
                  Your Google Sheets Web App Endpoint URL:
                </label>
                <div className="flex gap-2">
                  <input
                    type="url"
                    value={webhookUrl}
                    onChange={(e) => setWebhookUrl(e.target.value)}
                    placeholder="https://script.google.com/macros/s/.../exec"
                    className="flex-1 bg-slate-50 border border-slate-300 rounded-xl px-3.5 py-2.5 text-xs font-mono text-slate-800 focus:outline-none focus:ring-2 focus:ring-emerald-500"
                  />
                  <button
                    onClick={handleTestConnection}
                    disabled={testing || !webhookUrl.trim()}
                    className="px-4 py-2.5 bg-slate-800 hover:bg-slate-900 disabled:opacity-50 text-white rounded-xl text-xs font-bold transition flex items-center gap-1.5 shrink-0"
                  >
                    {testing ? (
                      <>
                        <RefreshCw className="w-3.5 h-3.5 animate-spin" />
                        <span>Testing...</span>
                      </>
                    ) : (
                      <>
                        <Radio className="w-3.5 h-3.5 text-emerald-400" />
                        <span>Test Connection</span>
                      </>
                    )}
                  </button>
                </div>
              </div>

              {/* Feedback Alert */}
              {testResult && (
                <div
                  className={`p-3.5 rounded-xl border text-xs flex items-center gap-2.5 ${
                    testResult.success
                      ? 'bg-emerald-50 border-emerald-300 text-emerald-900'
                      : 'bg-rose-50 border-rose-300 text-rose-900'
                  }`}
                >
                  {testResult.success ? (
                    <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0" />
                  ) : (
                    <AlertTriangle className="w-4 h-4 text-rose-600 shrink-0" />
                  )}
                  <span className="font-semibold">{testResult.message}</span>
                </div>
              )}

              {/* Auto-Sync Toggle & Action */}
              <div className="flex items-center justify-between p-4 bg-slate-50 border border-slate-200 rounded-2xl">
                <div className="flex items-center gap-2.5">
                  <input
                    type="checkbox"
                    id="autoSyncToggle"
                    checked={autoSyncEnabled}
                    onChange={(e) => {
                      setAutoSync(e.target.checked);
                      setAutoSyncEnabled(e.target.checked);
                    }}
                    className="w-4 h-4 text-emerald-600 rounded border-slate-300 focus:ring-emerald-500 cursor-pointer"
                  />
                  <label htmlFor="autoSyncToggle" className="text-xs font-bold text-slate-800 cursor-pointer">
                    Automatically sync every mark as I type
                  </label>
                </div>

                <button
                  onClick={handleSaveAndSyncNow}
                  disabled={manualSyncing || !webhookUrl.trim()}
                  className="px-5 py-2.5 bg-emerald-600 hover:bg-emerald-700 disabled:opacity-50 text-white rounded-xl text-xs font-bold transition flex items-center gap-2 shadow-md shadow-emerald-200"
                >
                  {manualSyncing ? (
                    <>
                      <RefreshCw className="w-4 h-4 animate-spin" />
                      <span>Syncing Google Sheet...</span>
                    </>
                  ) : (
                    <>
                      <Check className="w-4 h-4" />
                      <span>Save & Sync to Google Sheet Now</span>
                    </>
                  )}
                </button>
              </div>

            </div>
          )}

          {/* TAB 2: Apps Script Code */}
          {activeTab === 'script' && (
            <div className="space-y-4">
              <div className="bg-indigo-50 border border-indigo-200 rounded-2xl p-4 flex items-start gap-3">
                <Code2 className="w-5 h-5 text-indigo-600 shrink-0 mt-0.5" />
                <div className="text-xs text-indigo-900">
                  <p className="font-bold mb-1">
                    Google Apps Script Code (Ready to Paste):
                  </p>
                  <p className="text-indigo-800">
                    This script powers the live sync, handles automated batch cell updates, and enables the native <strong>`[+]` and `[-]`</strong> monthly column groupings right inside Google Sheets.
                  </p>
                </div>
              </div>

              <div className="relative">
                <textarea
                  readOnly
                  value={appsScriptCode}
                  className="w-full h-64 p-3 bg-slate-900 text-slate-200 font-mono text-xs rounded-2xl border border-slate-700 resize-none focus:outline-none"
                />
                <button
                  onClick={handleCopyCode}
                  className="absolute top-3 right-3 flex items-center gap-1.5 bg-indigo-600 hover:bg-indigo-700 text-white px-3 py-1.5 rounded-xl text-xs font-semibold shadow transition"
                >
                  {copiedCode ? (
                    <>
                      <Check className="w-4 h-4" />
                      <span>Copied!</span>
                    </>
                  ) : (
                    <>
                      <Copy className="w-4 h-4" />
                      <span>Copy Code.gs</span>
                    </>
                  )}
                </button>
              </div>
            </div>
          )}

          {/* TAB 3: Offline Excel */}
          {activeTab === 'excel' && (
            <div className="space-y-5 py-2">
              <div className="bg-slate-50 border border-slate-200 rounded-2xl p-5 text-center max-w-lg mx-auto">
                <div className="w-14 h-14 rounded-2xl bg-emerald-100 text-emerald-700 flex items-center justify-center mx-auto mb-3">
                  <Download className="w-7 h-7" />
                </div>
                <h3 className="text-base font-bold text-slate-800">Direct Workbook File</h3>
                <p className="text-xs text-slate-500 mt-1 mb-6">
                  Pre-configured with expandable monthly column groups, attendance/participation/homework caps, and class average formulas.
                </p>

                <button
                  onClick={handleDownloadExcel}
                  className="inline-flex items-center gap-2 bg-emerald-600 hover:bg-emerald-700 text-white px-6 py-3 rounded-xl text-sm font-bold shadow-md shadow-emerald-200 transition"
                >
                  <Download className="w-4 h-4" />
                  <span>Download "Teacher_Production_Gradebook.xlsx"</span>
                </button>
              </div>
            </div>
          )}

        </div>

        {/* Footer */}
        <div className="px-6 py-3.5 bg-slate-50 border-t border-slate-200 flex justify-end">
          <button
            onClick={onClose}
            className="px-4 py-2 bg-slate-200 hover:bg-slate-300 text-slate-700 rounded-xl text-xs font-bold transition"
          >
            Close
          </button>
        </div>

      </div>
    </div>
  );
};
