import React, { useState } from 'react';
import { X, Plus, Trash2, SlidersHorizontal, Check, AlertCircle } from 'lucide-react';
import { Category } from '../types/gradebook';

interface CategorySettingsModalProps {
  categories: Category[];
  onSaveCategories: (updatedCategories: Category[]) => void;
  onClose: () => void;
}

export const CategorySettingsModal: React.FC<CategorySettingsModalProps> = ({
  categories: initialCategories,
  onSaveCategories,
  onClose,
}) => {
  const [categories, setCategories] = useState<Category[]>(
    JSON.parse(JSON.stringify(initialCategories))
  );

  const [newCatName, setNewCatName] = useState('');
  const [newCatCap, setNewCatCap] = useState(20);

  const handleUpdateCap = (id: string, cap: number) => {
    setCategories((prev) =>
      prev.map((c) => (c.id === id ? { ...c, defaultCap: Math.max(1, cap) } : c))
    );
  };

  const handleUpdateName = (id: string, name: string) => {
    setCategories((prev) =>
      prev.map((c) => (c.id === id ? { ...c, name } : c))
    );
  };

  const handleDeleteCategory = (id: string) => {
    if (categories.length <= 1) {
      alert('You must have at least one category.');
      return;
    }
    setCategories((prev) => prev.filter((c) => c.id !== id));
  };

  const handleAddCategory = () => {
    if (!newCatName.trim()) return;
    const newCat: Category = {
      id: `cat-${Date.now()}`,
      name: newCatName.trim(),
      defaultCap: newCatCap > 0 ? newCatCap : 10,
      color: '#6366f1',
    };
    setCategories((prev) => [...prev, newCat]);
    setNewCatName('');
    setNewCatCap(20);
  };

  const totalCap = categories.reduce((sum, c) => sum + (c.defaultCap || 0), 0);

  const handleSave = () => {
    onSaveCategories(categories);
    onClose();
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-sm overflow-y-auto">
      <div className="bg-white rounded-3xl shadow-2xl border border-slate-200 w-full max-w-xl overflow-hidden transition-all">
        
        {/* Header */}
        <div className="px-6 py-4 border-b border-slate-200 bg-slate-900 text-white flex items-center justify-between">
          <div className="flex items-center gap-2.5">
            <SlidersHorizontal className="w-5 h-5 text-indigo-400" />
            <h2 className="text-base font-bold">Manage Categories & Caps</h2>
          </div>
          <button
            onClick={onClose}
            className="p-1.5 hover:bg-slate-800 rounded-lg text-slate-400 hover:text-white transition"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Body */}
        <div className="p-6 space-y-6">
          <div className="bg-indigo-50 border border-indigo-200 rounded-2xl p-4 flex items-center justify-between">
            <div>
              <span className="text-xs font-semibold text-indigo-900 block">
                Total Per-Lesson Maximum Cap
              </span>
              <span className="text-xs text-indigo-700">
                Sum of category points evaluated for each single lesson
              </span>
            </div>
            <div className="text-2xl font-black text-indigo-700">
              {totalCap} <span className="text-xs font-semibold text-indigo-500">pts / lesson</span>
            </div>
          </div>

          {/* Existing Categories List */}
          <div className="space-y-3">
            <span className="text-xs font-bold text-slate-700 uppercase tracking-wider block">
              Active Marking Categories
            </span>

            {categories.map((cat) => (
              <div
                key={cat.id}
                className="flex items-center gap-3 p-3 bg-slate-50 border border-slate-200 rounded-xl"
              >
                <div className="flex-1">
                  <input
                    type="text"
                    value={cat.name}
                    onChange={(e) => handleUpdateName(cat.id, e.target.value)}
                    className="w-full bg-white border border-slate-300 rounded-lg px-2.5 py-1.5 text-xs font-semibold text-slate-800 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                    placeholder="Category Name"
                  />
                </div>

                <div className="flex items-center gap-2">
                  <span className="text-xs text-slate-500 font-medium">Max Cap:</span>
                  <input
                    type="number"
                    min="1"
                    value={cat.defaultCap}
                    onChange={(e) => handleUpdateCap(cat.id, parseFloat(e.target.value) || 1)}
                    className="w-20 bg-white border border-slate-300 rounded-lg px-2.5 py-1.5 text-xs font-bold text-indigo-700 text-center focus:outline-none focus:ring-2 focus:ring-indigo-500"
                  />
                </div>

                <button
                  onClick={() => handleDeleteCategory(cat.id)}
                  className="p-1.5 text-slate-400 hover:text-rose-600 hover:bg-rose-50 rounded-lg transition"
                  title="Remove category"
                >
                  <Trash2 className="w-4 h-4" />
                </button>
              </div>
            ))}
          </div>

          {/* Add New Category */}
          <div className="border-t border-slate-200 pt-4">
            <span className="text-xs font-bold text-slate-700 uppercase tracking-wider block mb-2">
              Add New Category
            </span>
            <div className="flex items-center gap-2">
              <input
                type="text"
                value={newCatName}
                onChange={(e) => setNewCatName(e.target.value)}
                placeholder="e.g. Lab Reports, Pop Quiz, Project..."
                className="flex-1 bg-slate-50 border border-slate-300 rounded-lg px-3 py-2 text-xs text-slate-800 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                onKeyDown={(e) => e.key === 'Enter' && handleAddCategory()}
              />
              <input
                type="number"
                min="1"
                value={newCatCap}
                onChange={(e) => setNewCatCap(parseFloat(e.target.value) || 10)}
                placeholder="Cap"
                className="w-20 bg-slate-50 border border-slate-300 rounded-lg px-2 py-2 text-xs font-bold text-center text-slate-800 focus:outline-none focus:ring-2 focus:ring-indigo-500"
              />
              <button
                onClick={handleAddCategory}
                className="bg-slate-800 hover:bg-slate-900 text-white px-3 py-2 rounded-lg text-xs font-semibold flex items-center gap-1 transition"
              >
                <Plus className="w-4 h-4" />
                <span>Add</span>
              </button>
            </div>
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
            onClick={handleSave}
            className="px-5 py-2 bg-indigo-600 hover:bg-indigo-700 text-white rounded-xl text-xs font-bold transition flex items-center gap-1.5 shadow"
          >
            <Check className="w-4 h-4" />
            <span>Save Categories & Caps</span>
          </button>
        </div>

      </div>
    </div>
  );
};
