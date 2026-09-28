import React, { useState } from 'react';
import { X, Users, Check, AlertCircle } from 'lucide-react';
import { Student } from '../types/gradebook';

interface BulkAddStudentsModalProps {
  onAddStudents: (newStudents: Student[]) => void;
  onClose: () => void;
  existingCount: number;
}

export const BulkAddStudentsModal: React.FC<BulkAddStudentsModalProps> = ({
  onAddStudents,
  onClose,
  existingCount,
}) => {
  const [text, setText] = useState('');

  const handleInsert = () => {
    const lines = text
      .split('\n')
      .map((l) => l.trim())
      .filter((l) => l.length > 0);

    if (lines.length === 0) return;

    const startRoll = existingCount + 1;
    const students: Student[] = lines.map((line, idx) => {
      // Support comma or tab separated: "101, John Doe" or just "John Doe"
      const parts = line.split(/[,\t]/);
      let rollNo = String(startRoll + idx);
      let name = line;

      if (parts.length >= 2 && !isNaN(Number(parts[0].trim()))) {
        rollNo = parts[0].trim();
        name = parts.slice(1).join(',').trim();
      }

      return {
        id: `st-${Date.now()}-${idx}-${Math.random().toString(36).substr(2, 4)}`,
        name,
        rollNo,
      };
    });

    onAddStudents(students);
    onClose();
  };

  const lineCount = text
    .split('\n')
    .map((l) => l.trim())
    .filter((l) => l.length > 0).length;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-sm overflow-y-auto">
      <div className="bg-white rounded-3xl shadow-2xl border border-slate-200 w-full max-w-lg overflow-hidden transition-all">
        
        {/* Header */}
        <div className="px-6 py-4 border-b border-slate-200 bg-slate-900 text-white flex items-center justify-between">
          <div className="flex items-center gap-2.5">
            <Users className="w-5 h-5 text-indigo-400" />
            <h2 className="text-base font-bold">Bulk Paste Student Roster</h2>
          </div>
          <button
            onClick={onClose}
            className="p-1 hover:bg-slate-800 rounded-lg text-slate-400 hover:text-white transition"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Body */}
        <div className="p-6 space-y-4">
          <p className="text-xs text-slate-600">
            Paste your real class list below (one student per line, or copied from Excel / Google Sheets). Roll numbers will be automatically assigned:
          </p>

          <textarea
            autoFocus
            rows={10}
            value={text}
            onChange={(e) => setText(e.target.value)}
            placeholder={`Emma Davis\nLiam Johnson\nNoah Martinez\nOlivia Taylor\nWilliam Anderson`}
            className="w-full bg-slate-50 border border-slate-300 rounded-xl p-3 text-xs text-slate-900 font-medium focus:outline-none focus:ring-2 focus:ring-indigo-500 font-mono"
          />

          <div className="flex items-center justify-between text-xs text-slate-500">
            <span>Detected: <strong className="text-indigo-700">{lineCount}</strong> students</span>
            <span>Supports copy-paste directly from Google Sheets / Excel</span>
          </div>
        </div>

        {/* Footer */}
        <div className="px-6 py-4 bg-slate-50 border-t border-slate-200 flex justify-end gap-2">
          <button
            onClick={onClose}
            className="px-4 py-2 bg-white border border-slate-300 hover:bg-slate-100 text-slate-700 rounded-xl text-xs font-semibold transition"
          >
            Cancel
          </button>
          <button
            onClick={handleInsert}
            disabled={lineCount === 0}
            className="px-5 py-2 bg-indigo-600 hover:bg-indigo-700 disabled:opacity-50 text-white rounded-xl text-xs font-bold transition flex items-center gap-1.5 shadow"
          >
            <Check className="w-4 h-4" />
            <span>Insert {lineCount > 0 ? `${lineCount} Students` : 'Students'}</span>
          </button>
        </div>

      </div>
    </div>
  );
};
