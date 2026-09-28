import React, { useState } from 'react';
import { X, School, Plus, Check } from 'lucide-react';
import { ClassData } from '../types/gradebook';

interface ClassSettingsModalProps {
  onAddClass: (newClass: ClassData) => void;
  onClose: () => void;
}

export const ClassSettingsModal: React.FC<ClassSettingsModalProps> = ({
  onAddClass,
  onClose,
}) => {
  const [name, setName] = useState('');
  const [subject, setSubject] = useState('');
  const [gradeLevel, setGradeLevel] = useState('10th Grade');
  const [academicYear, setAcademicYear] = useState('2026-2027');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!name.trim()) return;

    const newClass: ClassData = {
      id: `class-${Date.now()}`,
      name: name.trim(),
      subject: subject.trim() || 'General',
      gradeLevel: gradeLevel.trim() || 'General',
      academicYear: academicYear.trim() || '2026-2027',
      categories: [
        { id: 'att', name: 'Attendance', defaultCap: 5, color: '#10b981' },
        { id: 'part', name: 'Participation', defaultCap: 10, color: '#6366f1' },
        { id: 'hw', name: 'Homework', defaultCap: 10, color: '#f59e0b' },
      ],
      months: [
        { id: 'sep', name: 'September', shortName: 'Sep', academicYear },
        { id: 'oct', name: 'October', shortName: 'Oct', academicYear },
        { id: 'nov', name: 'November', shortName: 'Nov', academicYear },
      ],
      lessons: [
        { id: `sep-l1-${Date.now()}`, monthId: 'sep', dayNumber: 1, date: 'Sep 02', title: 'Day 1' },
        { id: `sep-l2-${Date.now()}`, monthId: 'sep', dayNumber: 2, date: 'Sep 05', title: 'Day 2' },
        { id: `sep-l3-${Date.now()}`, monthId: 'sep', dayNumber: 3, date: 'Sep 09', title: 'Day 3' },
        { id: `sep-l4-${Date.now()}`, monthId: 'sep', dayNumber: 4, date: 'Sep 12', title: 'Day 4' },
      ],
      students: [],
      grades: {},
    };

    onAddClass(newClass);
    onClose();
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-sm overflow-y-auto">
      <div className="bg-white rounded-3xl shadow-2xl border border-slate-200 w-full max-w-md overflow-hidden transition-all">
        
        <div className="px-6 py-4 border-b border-slate-200 bg-slate-900 text-white flex items-center justify-between">
          <div className="flex items-center gap-2">
            <School className="w-5 h-5 text-indigo-400" />
            <h2 className="text-base font-bold">Create New Class</h2>
          </div>
          <button
            onClick={onClose}
            className="p-1 hover:bg-slate-800 rounded-lg text-slate-400 hover:text-white transition"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        <form onSubmit={handleSubmit} className="p-6 space-y-4">
          <div>
            <label className="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1">
              Class Name *
            </label>
            <input
              type="text"
              required
              autoFocus
              value={name}
              onChange={(e) => setName(e.target.value)}
              placeholder="e.g. 10th Grade - Biology"
              className="w-full bg-slate-50 border border-slate-300 rounded-xl px-3 py-2 text-sm text-slate-800 focus:outline-none focus:ring-2 focus:ring-indigo-500"
            />
          </div>

          <div className="grid grid-cols-2 gap-3">
            <div>
              <label className="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1">
                Subject
              </label>
              <input
                type="text"
                value={subject}
                onChange={(e) => setSubject(e.target.value)}
                placeholder="e.g. Science"
                className="w-full bg-slate-50 border border-slate-300 rounded-xl px-3 py-2 text-sm text-slate-800 focus:outline-none focus:ring-2 focus:ring-indigo-500"
              />
            </div>

            <div>
              <label className="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1">
                Academic Year
              </label>
              <input
                type="text"
                value={academicYear}
                onChange={(e) => setAcademicYear(e.target.value)}
                placeholder="2026-2027"
                className="w-full bg-slate-50 border border-slate-300 rounded-xl px-3 py-2 text-sm text-slate-800 focus:outline-none focus:ring-2 focus:ring-indigo-500"
              />
            </div>
          </div>

          <div className="bg-indigo-50 border border-indigo-200 rounded-xl p-3 text-xs text-indigo-900">
            This class will be initialized with default categories (Attendance: 10, Participation: 20, Homework: 30, Quiz: 40) and months, which you can customize anytime.
          </div>

          <div className="pt-2 flex justify-end gap-2">
            <button
              type="button"
              onClick={onClose}
              className="px-4 py-2 bg-white border border-slate-300 hover:bg-slate-100 text-slate-700 rounded-xl text-xs font-semibold transition"
            >
              Cancel
            </button>
            <button
              type="submit"
              className="px-5 py-2 bg-indigo-600 hover:bg-indigo-700 text-white rounded-xl text-xs font-bold transition flex items-center gap-1.5 shadow"
            >
              <Plus className="w-4 h-4" />
              <span>Create Class</span>
            </button>
          </div>
        </form>

      </div>
    </div>
  );
};
